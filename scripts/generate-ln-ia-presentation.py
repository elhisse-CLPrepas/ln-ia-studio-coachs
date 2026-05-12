from __future__ import annotations

import shutil
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "presentation" / "ln-ia-studio-coachs-webinaire-12-mai-2026.pptx"
ASSETS = ROOT / "assets" / "img"

SLIDE_W = 12192000
SLIDE_H = 6858000

COLORS = {
    "dark": "101820",
    "text": "1E2428",
    "cream": "F7F7F4",
    "paper": "FFFFFF",
    "gold": "F2C86B",
    "green": "A9DFBF",
    "soft_green": "E6F0E8",
}


def emu(x: float) -> int:
    return int(x * 914400)


def xml_text(text: str) -> str:
    return escape(text)


def paragraph(text: str, size: int, color: str, bold: bool = False) -> str:
    return (
        "<a:p>"
        f'<a:r><a:rPr lang="fr-FR" sz="{size * 100}"'
        f'{" b=\"1\"" if bold else ""}>'
        f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
        f'</a:rPr><a:t>{xml_text(text)}</a:t></a:r>'
        "</a:p>"
    )


def text_box(idx: int, name: str, text: str, x: float, y: float, w: float, h: float, size: int, color: str, bold: bool = False) -> str:
    paras = "".join(paragraph(line, size, color, bold) for line in text.splitlines())
    return f"""
      <p:sp>
        <p:nvSpPr><p:cNvPr id="{idx}" name="{xml_text(name)}"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:noFill/><a:ln><a:noFill/></a:ln>
        </p:spPr>
        <p:txBody><a:bodyPr wrap="square"/><a:lstStyle/>{paras}</p:txBody>
      </p:sp>
    """


def rect(idx: int, name: str, x: float, y: float, w: float, h: float, color: str, line: str | None = None) -> str:
    line_xml = f'<a:ln><a:solidFill><a:srgbClr val="{line}"/></a:solidFill></a:ln>' if line else "<a:ln><a:noFill/></a:ln>"
    return f"""
      <p:sp>
        <p:nvSpPr><p:cNvPr id="{idx}" name="{xml_text(name)}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
          <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>{line_xml}
        </p:spPr>
      </p:sp>
    """


def picture(idx: int, name: str, rid: str, x: float, y: float, w: float, h: float) -> str:
    return f"""
      <p:pic>
        <p:nvPicPr><p:cNvPr id="{idx}" name="{xml_text(name)}"/><p:cNvPicPr/><p:nvPr/></p:nvPicPr>
        <p:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>
        <p:spPr>
          <a:xfrm><a:off x="{emu(x)}" y="{emu(y)}"/><a:ext cx="{emu(w)}" cy="{emu(h)}"/></a:xfrm>
          <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
        </p:spPr>
      </p:pic>
    """


def slide_xml(background: str, shapes: list[str]) -> str:
    body = "\n".join(shapes)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="{background}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      {body}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>"""


def slide_rels(image_targets: list[str]) -> str:
    rels = [
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>'
    ]
    for index, target in enumerate(image_targets, start=2):
        rels.append(
            f'<Relationship Id="rId{index}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/{target}"/>'
        )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{''.join(rels)}</Relationships>"""


def base_shapes(number: int, dark: bool = False) -> list[str]:
    footer_color = COLORS["cream"] if dark else COLORS["text"]
    return [
        rect(2, "Accent", 0, 0, 0.16, 7.5, COLORS["gold"]),
        text_box(3, "Footer", "LN-IA Studio Coachs", 0.5, 7.05, 4.0, 0.25, 9, footer_color),
        text_box(4, "Number", f"{number} / 12", 12.1, 7.05, 0.7, 0.25, 9, footer_color),
    ]


def title_slide(number: int, kicker: str, title: str, subtitle: str) -> tuple[str, list[str]]:
    shapes = base_shapes(number, True)
    shapes.extend(
        [
            text_box(5, "Kicker", kicker, 0.75, 0.65, 7.0, 0.35, 13, COLORS["gold"], True),
            text_box(6, "Title", title, 0.75, 1.25, 8.2, 1.7, 40, "FFFFFF", True),
            text_box(7, "Subtitle", subtitle, 0.8, 3.25, 7.1, 0.9, 20, COLORS["cream"]),
            rect(8, "CTA", 0.8, 4.7, 4.3, 0.55, COLORS["green"]),
            text_box(9, "CTA Text", "Webinaire - Mardi 12 mai 2026 - 20h00 GMT+1", 1.0, 4.86, 3.9, 0.25, 13, COLORS["dark"], True),
        ]
    )
    return slide_xml(COLORS["dark"], shapes), []


def bullets_slide(number: int, kicker: str, title: str, bullets: list[str]) -> tuple[str, list[str]]:
    shapes = base_shapes(number)
    bullet_text = "\n".join(f"- {item}" for item in bullets)
    shapes.extend(
        [
            text_box(5, "Kicker", kicker, 0.75, 0.6, 7.0, 0.35, 12, "204B34", True),
            text_box(6, "Title", title, 0.75, 1.05, 8.4, 0.85, 30, COLORS["dark"], True),
            text_box(7, "Bullets", bullet_text, 1.0, 2.25, 8.4, 2.7, 20, COLORS["text"]),
            rect(8, "Note", 10.2, 2.1, 2.2, 2.2, COLORS["soft_green"], COLORS["green"]),
            text_box(9, "Note Text", "Repère participant\n\nNoter une action concrète à tester cette semaine.", 10.45, 2.35, 1.7, 1.55, 14, COLORS["dark"], True),
        ]
    )
    return slide_xml(COLORS["cream"], shapes), []


def image_slide(number: int, kicker: str, title: str, text: str, image_name: str) -> tuple[str, list[str]]:
    shapes = base_shapes(number, True)
    target = image_name
    shapes.extend(
        [
            text_box(5, "Kicker", kicker, 0.75, 0.6, 7.0, 0.35, 12, COLORS["gold"], True),
            text_box(6, "Title", title, 0.75, 1.05, 7.2, 0.9, 30, "FFFFFF", True),
            text_box(7, "Body", text, 0.8, 2.45, 5.3, 1.8, 18, COLORS["cream"]),
            picture(8, image_name, "rId2", 8.1, 1.45, 3.3, 3.3),
        ]
    )
    return slide_xml(COLORS["dark"], shapes), [target]


def content_types() -> str:
    slide_overrides = "".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, 13)
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


def presentation_xml() -> str:
    slide_ids = "".join(f'<p:sldId id="{255 + i}" r:id="rId{i + 1}"/>' for i in range(1, 13))
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst>
  <p:sldIdLst>{slide_ids}</p:sldIdLst>
  <p:sldSz cx="{SLIDE_W}" cy="{SLIDE_H}" type="wide"/>
  <p:notesSz cx="6858000" cy="9144000"/>
  <p:defaultTextStyle/>
</p:presentation>"""


def presentation_rels() -> str:
    rels = ['<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>']
    for i in range(1, 13):
        rels.append(f'<Relationship Id="rId{i + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>')
    rels.append('<Relationship Id="rId14" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>')
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{''.join(rels)}</Relationships>"""


SLIDE_MASTER = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>
  <p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles>
</p:sldMaster>"""

SLIDE_MASTER_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>"""

SLIDE_LAYOUT = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">
  <p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr></p:spTree></p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sldLayout>"""

SLIDE_LAYOUT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>"""

THEME = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="LN-IA">
  <a:themeElements>
    <a:clrScheme name="LN-IA"><a:dk1><a:srgbClr val="101820"/></a:dk1><a:lt1><a:srgbClr val="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="1E2428"/></a:dk2><a:lt2><a:srgbClr val="F7F7F4"/></a:lt2><a:accent1><a:srgbClr val="F2C86B"/></a:accent1><a:accent2><a:srgbClr val="A9DFBF"/></a:accent2><a:accent3><a:srgbClr val="204B34"/></a:accent3><a:accent4><a:srgbClr val="E6F0E8"/></a:accent4><a:accent5><a:srgbClr val="C8C1B5"/></a:accent5><a:accent6><a:srgbClr val="172027"/></a:accent6><a:hlink><a:srgbClr val="204B34"/></a:hlink><a:folHlink><a:srgbClr val="204B34"/></a:folHlink></a:clrScheme>
    <a:fontScheme name="LN-IA"><a:majorFont><a:latin typeface="Aptos Display"/></a:majorFont><a:minorFont><a:latin typeface="Aptos"/></a:minorFont></a:fontScheme>
    <a:fmtScheme name="LN-IA"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst><a:lnStyleLst><a:ln w="6350"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst><a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme>
  </a:themeElements>
</a:theme>"""


def build() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)

    media_map = {
        "programme-webinaire-atelier-ln-ia.png": ASSETS / "programme-webinaire-atelier-ln-ia.png",
        "fiche-vous-repartirez-avec.png": ASSETS / "fiche-vous-repartirez-avec.png",
    }

    slides = [
        title_slide(1, "Webinaire - 12 mai 2026", "Comment l'IA transforme le coaching", "Passer du coaching classique au coaching augmenté par IA, sans perdre l'humain."),
        bullets_slide(2, "Promesse", "Comprendre, pratiquer, transmettre", ["Comprendre le changement IA.", "Développer les skills IA indispensables.", "Garder un cadre humain, éthique et pédagogique.", "Repartir avec une méthode d'action."]),
        bullets_slide(3, "Pourquoi maintenant ?", "Le changement accélère", ["Le monde se transforme à grande vitesse.", "L'IA accélère les usages et les attentes.", "Les métiers changent : préparer, produire, vérifier, publier.", "Les coachs doivent apprendre à travailler avec ces nouveaux systèmes."]),
        bullets_slide(4, "Trois échelles", "Lire la transformation", ["Monde : IA, cloud, satellites, quantique.", "Personnel : mindset, habitudes, attention.", "Professionnel : développement moderne, production, publication."]),
        bullets_slide(5, "New Paradigm IA", "Une nouvelle manière de travailler", ["Intention claire.", "Dialogue avec le modèle.", "Production structurée.", "Vérification humaine.", "Correction et transmission."]),
        bullets_slide(6, "Skills IA", "Les compétences indispensables", ["Formuler une intention claire.", "Écrire un prompt utile.", "Relancer avec des critères.", "Vérifier, corriger et documenter.", "Produire et publier."]),
        bullets_slide(7, "Coach augmenté", "Responsabilité humaine, puissance IA", ["Le coach augmenté ne délègue pas sa responsabilité.", "Il prépare mieux.", "Il structure et simule.", "Il synthétise et transmet.", "Il garde l'éthique au centre."]),
        image_slide(8, "Atelier pratique", "Optimiser une landing page", "Cas pratique : passer d'une intention à un support clair, ciblé et publiable avec l'aide de l'IA.", "programme-webinaire-atelier-ln-ia.png"),
        bullets_slide(9, "Grille d'analyse", "Observer avant d'améliorer", ["Public cible.", "Promesse et titre.", "Programme et preuves.", "Visuels et appel à l'action.", "Mobile, accessibilité et éthique."]),
        bullets_slide(10, "Exercice", "Améliorer une section avec l'IA", ["Choisir une section de la page.", "Formuler l'intention.", "Demander une amélioration ciblée.", "Expliquer ce qui a changé.", "Vérifier la qualité."]),
        image_slide(11, "Ce que vous emportez", "Vision, méthode et action", "Vous repartez avec une vision claire, des skills IA, des prompts, une grille d'analyse et une action à pratiquer.", "fiche-vous-repartirez-avec.png"),
        title_slide(12, "Appel à l'action", "Rejoindre la communauté et pratiquer", "Cette semaine : choisir une compétence IA, produire un livrable concret, puis partager le résultat avec la communauté LN-IA."),
    ]

    if OUT.exists():
        OUT.unlink()

    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as pptx:
        pptx.writestr("[Content_Types].xml", content_types())
        pptx.writestr("_rels/.rels", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>""")
        pptx.writestr("docProps/app.xml", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"><Application>LN-IA Generator</Application><PresentationFormat>Widescreen</PresentationFormat><Slides>12</Slides></Properties>""")
        pptx.writestr("docProps/core.xml", """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>LN-IA Studio Coachs - Webinaire 12 mai 2026</dc:title><dc:creator>LAB-NUMERIQUE-IA</dc:creator><cp:lastModifiedBy>Codex</cp:lastModifiedBy></cp:coreProperties>""")
        pptx.writestr("ppt/presentation.xml", presentation_xml())
        pptx.writestr("ppt/_rels/presentation.xml.rels", presentation_rels())
        pptx.writestr("ppt/slideMasters/slideMaster1.xml", SLIDE_MASTER)
        pptx.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", SLIDE_MASTER_RELS)
        pptx.writestr("ppt/slideLayouts/slideLayout1.xml", SLIDE_LAYOUT)
        pptx.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", SLIDE_LAYOUT_RELS)
        pptx.writestr("ppt/theme/theme1.xml", THEME)

        copied_media = set()
        for index, (xml, images) in enumerate(slides, start=1):
            pptx.writestr(f"ppt/slides/slide{index}.xml", xml)
            pptx.writestr(f"ppt/slides/_rels/slide{index}.xml.rels", slide_rels(images))
            for image in images:
                if image not in copied_media:
                    source = media_map[image]
                    pptx.writestr(f"ppt/media/{image}", source.read_bytes())
                    copied_media.add(image)

    print(OUT)


if __name__ == "__main__":
    build()
