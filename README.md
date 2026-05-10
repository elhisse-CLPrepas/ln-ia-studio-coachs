# LAB-NUMÉRIQUE-IA - Studio Coachs

Landing page no-framework pour le webinaire **LN-IA Studio Coachs**.

Objectif : publier une page HTML/CSS/JavaScript simple sur GitHub Pages afin de présenter le webinaire, son programme, ses visuels, le lien WhatsApp et les informations de participation.

## Structure

```text
ln-ia-studio-coachs/
|-- index.html
|-- webinaire.html
|-- README.md
|-- .gitignore
|-- BRIEF-CODEX.md
|-- ROADMAP.md
|-- CHANGELOG.md
|-- LICENSE
|-- assets/
|   |-- css/
|   |   `-- style.css
|   |-- js/
|   |   `-- app.js
|   `-- img/
|-- share/
|   |-- message-facebook.txt
|   `-- whatsapp.txt
|-- data/
`-- docs/
```

## Contenu de la landing page

La page comprend :

- le titre du webinaire ;
- les métadonnées SEO et Open Graph de base ;
- le nouveau logo LN-IA ;
- une présentation du changement à l'échelle du monde ;
- le public cible ;
- le programme en deux parties ;
- l'intervenant ;
- une fiche participant ;
- un bouton WhatsApp ;
- un QR code intégré dans le visuel participant ;
- une FAQ ;
- un appel à l'action final.

## Formation et atelier

La version `v0.2.0` amorce la transformation de la landing page en base de formation.

Supports en préparation :

- `docs/atelier/programme-formation-ln-ia-sc.md`
- `docs/atelier/deroule-atelier-ln-ia-sc.md`
- `docs/atelier/checklist-animateur-ln-ia-sc.md`
- `docs/atelier/fiche-participant-ln-ia-sc.md`
- `docs/atelier/prompts-atelier-ln-ia-sc.md`
- `docs/atelier/grille-analyse-landing-page.md`
- `docs/atelier/evaluation-formation-ln-ia-sc.md`
- `docs/atelier/plan-slides-ln-ia-sc.md`
- `docs/atelier/session-2h-ln-ia-sc.md`

## Utilisation locale

Ouvrir directement `index.html` dans un navigateur.

Aucun framework, build ou serveur local n'est nécessaire.

## Workflow Git simple

Vérifier l'état du projet :

```bash
git status
```

Ajouter les fichiers modifiés :

```bash
git add index.html webinaire.html README.md CHANGELOG.md assets/css/style.css assets/js/app.js assets/img share/message-facebook.txt share/whatsapp.txt
```

Créer un commit :

```bash
git commit -m "Improve LN-IA webinar landing page"
```

Créer un tag de version :

```bash
git tag v0.1.3
```

Pousser vers GitHub :

```bash
git push origin main
git push origin v0.1.3
```

## Publication GitHub Pages

Sur GitHub en français :

1. Ouvrir le dépôt.
2. Aller dans **Paramètres**.
3. Ouvrir **Pages**.
4. Dans **Source**, choisir **Déployer à partir d'une branche**.
5. Sélectionner la branche `main`.
6. Choisir le dossier `/root`.
7. Cliquer sur **Enregistrer**.

GitHub Pages publie les fichiers statiques du dépôt. Pour ce projet, `index.html` doit rester à la racine de la branche publiée.

Ne pas renseigner de domaine personnalisé pour le moment. L'adresse gratuite sera fournie par GitHub Pages.

## Versions

- `v0.1.0` : squelette initial.
- `v0.1.1` : landing page webinaire avec visuels, programme, fiche participant et CTA WhatsApp.
- `v0.1.2` : consolidation GitHub Pages, README workflow, FAQ et message Facebook.
- `v0.1.3` : amélioration du logo, des titres, des accents, du contraste et du responsive mobile.
- `v0.2.0` : amorçage de la formation et des supports d'atelier.

## Sources

Documents de cadrage :

- `guide_nouveaux_comportemant.docx`
- `document_technique_depot_LN_IA_SC.docx`
- `guide_orchestration_LN_IA_SC.docx`
- `guide_chef_atelier.docx`

Documentation utile :

- GitHub Pages : https://docs.github.com/pages
