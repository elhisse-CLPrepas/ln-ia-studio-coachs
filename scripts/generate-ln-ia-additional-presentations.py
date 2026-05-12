from __future__ import annotations

import importlib.util
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "img"
OUT_DIR = ROOT / "docs" / "presentation"
BASE_PATH = ROOT / "scripts" / "generate-ln-ia-presentation.py"

spec = importlib.util.spec_from_file_location("deckbase", BASE_PATH)
deckbase = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(deckbase)

COLORS = deckbase.COLORS
SLIDE_W = deckbase.SLIDE_W
SLIDE_H = deckbase.SLIDE_H


def content_types(count: int) -> str:
    slide_overrides = "".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Default Extension="png" ContentType="image/png"/>
  <Default Extension="jpg" ContentType="image/jpeg"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
  {slide_overrides}
</Types>"""


def presentation_xml(count: int) -> str:
    slide_ids = "".join(f'<p:sldId id="{255 + i}" r:id="rId{i + 1}"/>' for i in range(1, count + 1))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
  <p:sldIdLst>{slide_ids}</p:sldIdLst>
  <p:sldSz cx="{SLIDE_W}" cy="{SLIDE_H}" type="wide"/>
  <p:notesSz cx="6858000" cy="9144000"/>
  <p:defaultTextStyle/>
</p:presentation>"""


def presentation_rels(count: int) -> str:
    rels = ['<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>']
    for i in range(1, count + 1):
        rels.append(f'<Relationship Id="rId{i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>')
    rels.append(f'<Relationship Id="rId{count + 2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>')
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{''.join(rels)}</Relationships>"""


def base_shapes(number: int, total: int, dark: bool = False) -> list[str]:
    footer_color = COLORS["cream"] if dark else COLORS["text"]
    return [
        deckbase.rect(2, "Accent", 0, 0, 0.16, 7.5, COLORS["gold"]),
        deckbase.text_box(3, "Footer", "LN-IA Studio Coachs", 0.5, 7.05, 4.0, 0.25, 9, footer_color),
        deckbase.text_box(4, "Number", f"{number} / {total}", 12.05, 7.05, 0.85, 0.25, 9, footer_color),
    ]


def title_slide(number: int, total: int, kicker: str, title: str, subtitle: str) -> tuple[str, list[str]]:
    shapes = base_shapes(number, total, True)
    shapes.extend([
        deckbase.text_box(5, "Kicker", kicker, 0.75, 0.65, 8.0, 0.35, 13, COLORS["gold"], True),
        deckbase.text_box(6, "Title", title, 0.75, 1.22, 8.5, 1.8, 38, "FFFFFF", True),
        deckbase.text_box(7, "Subtitle", subtitle, 0.8, 3.28, 8.1, 1.0, 19, COLORS["cream"]),
        deckbase.rect(8, "Signal", 9.7, 1.22, 2.35, 2.35, COLORS["green"]),
        deckbase.text_box(9, "Signal Text", "Vision\nMéthode\nProduction", 10.05, 1.72, 1.65, 1.1, 20, COLORS["dark"], True),
    ])
    return deckbase.slide_xml(COLORS["dark"], shapes), []


def bullets_slide(number: int, total: int, kicker: str, title: str, bullets: list[str], note: str = "Action participant\n\nNoter une application directe.") -> tuple[str, list[str]]:
    shapes = base_shapes(number, total)
    shapes.extend([
        deckbase.text_box(5, "Kicker", kicker, 0.75, 0.55, 8.0, 0.35, 12, "204B34", True),
        deckbase.text_box(6, "Title", title, 0.75, 0.98, 8.6, 0.9, 29, COLORS["dark"], True),
        deckbase.text_box(7, "Bullets", "\n".join(f"- {item}" for item in bullets), 1.0, 2.12, 8.35, 2.95, 18, COLORS["text"]),
        deckbase.rect(8, "Note", 10.15, 2.0, 2.3, 2.35, COLORS["soft_green"], COLORS["green"]),
        deckbase.text_box(9, "Note Text", note, 10.42, 2.32, 1.74, 1.5, 14, COLORS["dark"], True),
    ])
    return deckbase.slide_xml(COLORS["cream"], shapes), []


def process_slide(number: int, total: int, kicker: str, title: str, steps: list[str]) -> tuple[str, list[str]]:
    shapes = base_shapes(number, total, True)
    shapes.extend([
        deckbase.text_box(5, "Kicker", kicker, 0.75, 0.55, 8.0, 0.35, 12, COLORS["gold"], True),
        deckbase.text_box(6, "Title", title, 0.75, 0.98, 8.9, 0.9, 29, "FFFFFF", True),
    ])
    x = 0.85
    for i, step in enumerate(steps, start=1):
        shapes.append(deckbase.rect(10 + i, f"Step {i}", x, 2.35, 2.15, 1.2, COLORS["green"]))
        shapes.append(deckbase.text_box(20 + i, f"StepText {i}", f"{i}\n{step}", x + 0.22, 2.55, 1.72, 0.72, 16, COLORS["dark"], True))
        x += 2.35
    return deckbase.slide_xml(COLORS["dark"], shapes), []


def image_slide(number: int, total: int, kicker: str, title: str, text: str, image_name: str) -> tuple[str, list[str]]:
    shapes = base_shapes(number, total, True)
    shapes.extend([
        deckbase.text_box(5, "Kicker", kicker, 0.75, 0.55, 8.0, 0.35, 12, COLORS["gold"], True),
        deckbase.text_box(6, "Title", title, 0.75, 0.98, 7.1, 0.9, 29, "FFFFFF", True),
        deckbase.text_box(7, "Body", text, 0.8, 2.35, 5.4, 1.9, 18, COLORS["cream"]),
        deckbase.picture(8, image_name, "rId2", 8.05, 1.35, 3.35, 3.35),
    ])
    return deckbase.slide_xml(COLORS["dark"], shapes), [image_name]


def cards_slide(number: int, total: int, kicker: str, title: str, cards: list[tuple[str, str]]) -> tuple[str, list[str]]:
    shapes = base_shapes(number, total)
    shapes.extend([
        deckbase.text_box(5, "Kicker", kicker, 0.75, 0.55, 8.0, 0.35, 12, "204B34", True),
        deckbase.text_box(6, "Title", title, 0.75, 0.98, 8.9, 0.9, 29, COLORS["dark"], True),
    ])
    positions = [(0.9, 2.15), (3.55, 2.15), (6.2, 2.15), (8.85, 2.15), (2.2, 4.0), (4.85, 4.0), (7.5, 4.0)]
    for index, (label, body) in enumerate(cards):
        x, y = positions[index]
        shapes.append(deckbase.rect(10 + index, f"Card {index}", x, y, 2.22, 1.15, "FFFFFF", "C8C1B5"))
        shapes.append(deckbase.rect(30 + index, f"CardAccent {index}", x, y, 0.12, 1.15, COLORS["green"]))
        shapes.append(deckbase.text_box(50 + index, f"CardText {index}", f"{label}\n{body}", x + 0.28, y + 0.18, 1.68, 0.78, 12, COLORS["text"], index < 4))
    return deckbase.slide_xml(COLORS["cream"], shapes), []


def comparison_slide(number: int, total: int, kicker: str, title: str, left_title: str, left_items: list[str], right_title: str, right_items: list[str]) -> tuple[str, list[str]]:
    shapes = base_shapes(number, total, True)
    shapes.extend([
        deckbase.text_box(5, "Kicker", kicker, 0.75, 0.55, 8.0, 0.35, 12, COLORS["gold"], True),
        deckbase.text_box(6, "Title", title, 0.75, 0.98, 8.8, 0.85, 29, "FFFFFF", True),
        deckbase.rect(7, "LeftPanel", 0.85, 2.0, 5.25, 3.1, "FFFFFF"),
        deckbase.rect(8, "RightPanel", 6.35, 2.0, 5.25, 3.1, COLORS["green"]),
        deckbase.text_box(9, "LeftTitle", left_title, 1.15, 2.28, 4.5, 0.35, 17, COLORS["dark"], True),
        deckbase.text_box(10, "LeftItems", "\n".join(f"- {item}" for item in left_items), 1.18, 2.88, 4.45, 1.7, 14, COLORS["text"]),
        deckbase.text_box(11, "RightTitle", right_title, 6.65, 2.28, 4.5, 0.35, 17, COLORS["dark"], True),
        deckbase.text_box(12, "RightItems", "\n".join(f"- {item}" for item in right_items), 6.68, 2.88, 4.45, 1.7, 14, COLORS["dark"]),
    ])
    return deckbase.slide_xml(COLORS["dark"], shapes), []


def timeline_slide(number: int, total: int, kicker: str, title: str, steps: list[tuple[str, str]]) -> tuple[str, list[str]]:
    shapes = base_shapes(number, total)
    shapes.extend([
        deckbase.text_box(5, "Kicker", kicker, 0.75, 0.55, 8.0, 0.35, 12, "204B34", True),
        deckbase.text_box(6, "Title", title, 0.75, 0.98, 8.8, 0.85, 29, COLORS["dark"], True),
        deckbase.rect(7, "Line", 1.0, 3.0, 10.8, 0.06, COLORS["gold"]),
    ])
    x = 1.0
    for index, (period, label) in enumerate(steps):
        shapes.append(deckbase.rect(20 + index, f"Dot {index}", x, 2.65, 1.35, 0.7, COLORS["dark"]))
        shapes.append(deckbase.text_box(40 + index, f"Period {index}", period, x + 0.12, 2.83, 1.1, 0.2, 11, "FFFFFF", True))
        shapes.append(deckbase.text_box(60 + index, f"Label {index}", label, x - 0.05, 3.58, 1.55, 0.55, 13, COLORS["text"], True))
        x += 2.25
    return deckbase.slide_xml(COLORS["cream"], shapes), []


def write_deck(path: Path, title: str, slides: list[tuple[str, list[str]]]) -> None:
    media_paths = {
        "programme-webinaire-atelier-ln-ia.png": ASSETS / "programme-webinaire-atelier-ln-ia.png",
        "fiche-vous-repartirez-avec.png": ASSETS / "fiche-vous-repartirez-avec.png",
        "affiche-webinaire-mardi-12-mai-2026.png": ASSETS / "affiche-webinaire-mardi-12-mai-2026.png",
    }
    if path.exists():
        path.unlink()
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as pptx:
        count = len(slides)
        pptx.writestr("[Content_Types].xml", content_types(count))
        pptx.writestr("_rels/.rels", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>""")
        pptx.writestr("docProps/app.xml", f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>LN-IA Generator</Application><PresentationFormat>Widescreen</PresentationFormat><Slides>{count}</Slides></Properties>""")
        pptx.writestr("docProps/core.xml", f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>{deckbase.xml_text(title)}</dc:title><dc:creator>LAB-NUMERIQUE-IA</dc:creator><cp:lastModifiedBy>Codex</cp:lastModifiedBy></cp:coreProperties>""")
        pptx.writestr("ppt/presentation.xml", presentation_xml(count))
        pptx.writestr("ppt/_rels/presentation.xml.rels", presentation_rels(count))
        pptx.writestr("ppt/slideMasters/slideMaster1.xml", deckbase.SLIDE_MASTER)
        pptx.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", deckbase.SLIDE_MASTER_RELS)
        pptx.writestr("ppt/slideLayouts/slideLayout1.xml", deckbase.SLIDE_LAYOUT)
        pptx.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", deckbase.SLIDE_LAYOUT_RELS)
        pptx.writestr("ppt/theme/theme1.xml", deckbase.THEME)
        copied_media = set()
        for index, (xml, images) in enumerate(slides, start=1):
            pptx.writestr(f"ppt/slides/slide{index}.xml", xml)
            pptx.writestr(f"ppt/slides/_rels/slide{index}.xml.rels", deckbase.slide_rels(images))
            for image in images:
                if image not in copied_media:
                    pptx.writestr(f"ppt/media/{image}", media_paths[image].read_bytes())
                    copied_media.add(image)


def analyze_source_pptx() -> str:
    source = OUT_DIR / "presentation-lab-num-ctm.pptx"
    if not source.exists():
        return "Source non trouvée."
    ns = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
    with zipfile.ZipFile(source) as z:
        slide_names = sorted(
            [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
            key=lambda n: int(re.search(r"slide(\d+)\.xml", n).group(1)),
        )
        lines = [
            "# Analyse - presentation-lab-num-ctm.pptx",
            "",
            f"- Fichier source : `{source.name}`",
            f"- Nombre de slides : {len(slide_names)}",
            f"- Médias embarqués : {len([n for n in z.namelist() if n.startswith('ppt/media/')])}",
            "",
            "## Fil narratif détecté",
            "",
            "- Ouverture : LAB-NUM-CTM, pourquoi, c'est quoi, pour qui, comment.",
            "- Problématique : accélération numérique, dispersion, transmission.",
            "- Réponse : laboratoire collectif pour apprendre en produisant.",
            "- Axes : pourquoi, quoi, public, méthode.",
            "- Conclusion : challenge 100 jours et décision de lancement.",
            "",
            "## Adaptation LN-IA proposée",
            "",
            "- Remplacer CTM par LN-IA Studio Coachs.",
            "- Déplacer l'objet vers coaching augmenté, facilitation et IA.",
            "- Garder la logique laboratoire, mémoire, livrables, communauté.",
            "- Ajouter les modèles IA, la landing page, GitHub et le kit atelier.",
            "",
        ]
        lines.append("## Aperçu texte par slide")
        for slide in slide_names:
            root = ET.fromstring(z.read(slide))
            texts = [t.text.strip() for t in root.findall(".//a:t", ns) if t.text and t.text.strip()]
            number = re.search(r"slide(\d+)\.xml", slide).group(1)
            lines.append("")
            lines.append(f"### Slide {number}")
            lines.extend([f"- {item}" for item in texts[:8]])
    return "\n".join(lines) + "\n"


def build_lab_adapted() -> None:
    total = 21
    slides = [
        title_slide(1, total, "Ouverture", "Laboratoire LN-IA Studio Coachs", "Transformer le coaching augmenté par IA en méthode, supports, communauté et productions versionnées."),
        bullets_slide(2, total, "Problématique", "Pourquoi maintenant ?", ["L'IA transforme apprendre, produire et transmettre.", "Les coachs doivent développer de nouveaux comportements.", "Les supports se dispersent sans cadre de capitalisation.", "LN-IA transforme les échanges en livrables réutilisables."]),
        bullets_slide(3, total, "Risque actuel", "Sans cadre, la mémoire atelier se perd", ["Prompts isolés et difficiles à retrouver.", "Savoir-faire non documenté.", "Présentations et supports non versionnés.", "Difficulté à reprendre un projet après la séance."]),
        bullets_slide(4, total, "Réponse LN-IA", "Créer un laboratoire d'orchestration IA", ["Produire : pages, guides, slides, prompts.", "Documenter : méthodes, décisions, critères.", "Publier : GitHub Pages, releases, supports.", "Archiver : mémoire commune et prochaines actions."]),
        title_slide(5, total, "Axe 1 - Pourquoi ?", "La compétence IA devient une compétence de base", "Comprendre, pratiquer et transmettre devient indispensable pour coachs, formateurs et managers."),
        process_slide(6, total, "Changement de paradigme", "Le coaching devient un système de production", ["Intention", "Dialogue", "Production", "Vérification", "Transmission"]),
        bullets_slide(7, total, "Enjeu collectif", "Une communauté qui apprend en produisant", ["Culture IA commune.", "Talents et rôles visibles.", "Patrimoine utile : fiches, slides, prompts.", "Progression mesurable par livrables."]),
        image_slide(8, total, "Valeur attendue", "Ce que LN-IA doit produire", "Méthode commune, kit atelier, présentations professionnelles, landing page optimisée et releases GitHub documentées.", "fiche-vous-repartirez-avec.png"),
        title_slide(9, total, "Axe 2 - C'est quoi ?", "Un atelier augmenté par IA", "Un environnement organisé pour apprendre, produire, documenter, publier et transmettre."),
        cards_slide(10, total, "Composants", "Outils, méthodes, contenus, personnes", [("GitHub", "mémoire"), ("VS Code", "production"), ("IA", "assistance"), ("Zoom", "atelier"), ("Docs", "guides"), ("PPTX", "transmission"), ("Releases", "versions")]),
        bullets_slide(11, total, "Trois piliers", "Comprendre, exécuter, appliquer", ["Vision : changement IA et New Paradigm IA.", "Manuel : déroulé, checklist, script.", "Référentiel : prompts, grilles, modèles.", "Pratique : landing page et livrable réel."]),
        image_slide(12, total, "Livrables concrets", "La crédibilité vient des productions visibles", "Landing page publiée, kit atelier complet, supports de facilitation, présentations PPTX et notes de release GitHub.", "programme-webinaire-atelier-ln-ia.png"),
        title_slide(13, total, "Axe 3 - Pour qui ?", "Coachs, managers, formateurs, responsables", "Le laboratoire est accessible à plusieurs profils, avec des niveaux d'entrée différents."),
        cards_slide(14, total, "Rôles possibles", "Contribuer sans être développeur", [("Rédiger", "clarifier"), ("Relire", "qualité"), ("Tester", "prompt"), ("Analyser", "page"), ("Créer", "visuel"), ("Animer", "groupe"), ("Documenter", "trace")]),
        bullets_slide(15, total, "Bénéfices par profil", "Chaque participant gagne en autonomie", ["Coach : préparer, simuler, synthétiser.", "Manager : piloter, cadrer, décider.", "Formateur : transmettre et évaluer.", "Communauté : capitaliser et publier."]),
        title_slide(16, total, "Axe 4 - Comment ?", "Commencer simple, produire vite, documenter", "Une routine courte, des mini-projets, des supports et des releases."),
        bullets_slide(17, total, "Kit atelier comme moteur", "Un programme d'action prêt à animer", ["Guide animateur.", "Cartes de facilitation.", "Sélection des modèles IA.", "Plan de slides.", "Grille landing page.", "Prompt maître."]),
        process_slide(18, total, "Méthode de travail", "Comprendre, pratiquer, documenter, partager", ["Objectif", "Prompt", "Livrable", "Validation", "Release"]),
        timeline_slide(19, total, "Challenge 100 jours", "Transformer la vision en mouvement", [("J1-J10", "Alignement"), ("J11-J35", "Initiation"), ("J36-J70", "Production"), ("J71-J90", "Consolidation"), ("J91-J100", "Restitution")]),
        bullets_slide(20, total, "Décision", "Passer de la vision à l'action", ["Valider l'orientation atelier.", "Identifier les volontaires.", "Choisir un calendrier simple.", "Lancer la première production.", "Suivre les releases."]),
        title_slide(21, total, "Clôture", "LN-IA : orchestrer l'IA pour amplifier l'impact humain", "La prochaine étape : animer, produire, publier, puis améliorer à partir des retours participants."),
    ]
    write_deck(OUT_DIR / "ln-ia-studio-coachs-lab-numerique-adapte.pptx", "LN-IA Studio Coachs - Laboratoire adapté", slides)


def build_landing_practice() -> None:
    total = 14
    slides = [
        title_slide(1, total, "Partie pratique", "Optimiser une landing page avec l'IA", "Transformer une intention en page claire, ciblée, vérifiable et publiable."),
        image_slide(2, total, "Contexte", "La landing page LN-IA", "Point de départ : une page statique publiée, avec visuels, programme, CTA WhatsApp et kit atelier associé.", "affiche-webinaire-mardi-12-mai-2026.png"),
        bullets_slide(3, total, "Objectif", "Ce que l'optimisation doit améliorer", ["Clarté du public cible.", "Force de la promesse.", "Hiérarchie des sections.", "Lisibilité mobile.", "CTA plus évident.", "Éthique et ton humain."]),
        bullets_slide(4, total, "Grille", "Observer avant de corriger", ["Public.", "Promesse.", "Titre.", "Programme.", "Visuels.", "CTA.", "Mobile.", "Éthique."]),
        process_slide(5, total, "Méthode", "Le cycle d'orchestration IA", ["Contexte", "Prompt", "Production", "Vérification", "Publication"]),
        bullets_slide(6, total, "Diagnostic", "Questions à poser à la page", ["Comprend-on pour qui elle est faite ?", "Le bénéfice est-il visible en 5 secondes ?", "Le CTA est-il répété au bon moment ?", "Les visuels soutiennent-ils vraiment le message ?", "Le texte inspire-t-il confiance ?"]),
        bullets_slide(7, total, "Prompt maître", "Demander une amélioration ciblée", ["Rôle : expert landing pages pédagogiques.", "Contexte : LN-IA Studio Coachs.", "Public : coachs, managers, formateurs.", "Tâche : diagnostiquer et proposer une version améliorée.", "Contraintes : humain, clair, mobile, éthique."]),
        comparison_slide(8, total, "Avant / Après", "Ce que l'IA doit produire", "Avant", ["message diffus", "CTA peu visible", "hiérarchie à renforcer", "mobile à vérifier"], "Après", ["promesse claire", "CTA direct", "sections lisibles", "validation humaine"]),
        bullets_slide(9, total, "Exercice participant", "Améliorer une section", ["Choisir une section.", "Coller le texte actuel.", "Formuler l'intention.", "Lancer le prompt.", "Comparer avant/après.", "Valider humainement."]),
        image_slide(10, total, "Programme", "Relier la pratique au webinaire", "La landing page devient un cas concret pour apprendre la méthode : intention, production, vérification, correction.", "programme-webinaire-atelier-ln-ia.png"),
        cards_slide(11, total, "Critères qualité", "Ce qui rend la page meilleure", [("Clarté", "public"), ("Promesse", "bénéfice"), ("Titre", "mémorable"), ("CTA", "visible"), ("Mobile", "lisible"), ("Éthique", "humain"), ("Preuve", "crédible")]),
        bullets_slide(12, total, "Publication", "Passer de l'amélioration à la release", ["Modifier HTML/CSS si nécessaire.", "Vérifier localement.", "Commit Git.", "Tag de version.", "Push GitHub.", "Documenter dans le changelog."]),
        image_slide(13, total, "Sortie attendue", "Ce que le participant emporte", "Un diagnostic, un prompt, une version améliorée, une checklist et une action à pratiquer cette semaine.", "fiche-vous-repartirez-avec.png"),
        title_slide(14, total, "Clôture pratique", "L'IA ne remplace pas le jugement : elle structure l'action", "Le participant repart avec une méthode réutilisable pour ses propres pages, offres et supports pédagogiques."),
    ]
    write_deck(OUT_DIR / "ln-ia-atelier-landing-page-optimisee.pptx", "LN-IA - Atelier landing page optimisée", slides)


def build() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "analyse-presentation-lab-num-ctm.md").write_text(analyze_source_pptx(), encoding="utf-8")
    build_lab_adapted()
    build_landing_practice()
    print(OUT_DIR / "ln-ia-studio-coachs-lab-numerique-adapte.pptx")
    print(OUT_DIR / "ln-ia-atelier-landing-page-optimisee.pptx")


if __name__ == "__main__":
    build()
