# LAB-NUMERIQUE-IA - Studio Coachs

Landing page no-framework pour le webinaire **LN-IA Studio Coachs**.

Objectif : publier une page HTML/CSS/JavaScript simple sur GitHub Pages pour presenter le webinaire, son programme, les visuels, le lien WhatsApp et les informations de participation.

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

- titre du webinaire ;
- programme en deux parties ;
- intervenant et porteur de l'atelier ;
- bouton WhatsApp ;
- QR code integre dans la fiche participant ;
- FAQ ;
- appel a l'action final ;
- metadonnees SEO et Open Graph de base.

## Utilisation locale

Ouvrir directement `index.html` dans un navigateur.

Aucun framework, build ou serveur local n'est necessaire.

## Workflow Git simple

Verifier l'etat du projet :

```bash
git status
```

Ajouter les fichiers :

```bash
git add index.html README.md .gitignore assets/css/style.css assets/js/app.js assets/img share/message-facebook.txt share/whatsapp.txt
```

Creer un commit :

```bash
git commit -m "Prepare LN-IA webinar landing page"
```

Creer un tag de version :

```bash
git tag v0.1.0
```

Pousser vers GitHub :

```bash
git push -u origin main
git push origin v0.1.0
```

## Publication GitHub Pages

Sur GitHub :

1. Ouvrir le depot.
2. Aller dans `Settings`.
3. Ouvrir `Pages`.
4. Choisir `Deploy from a branch`.
5. Selectionner la branche a publier, par exemple `main`.
6. Choisir le dossier `/root`.
7. Enregistrer.

GitHub Pages publie les fichiers statiques du depot. Pour ce projet, `index.html` doit rester a la racine de la branche publiee.

## Versions

- `v0.1.0` : squelette initial.
- `v0.1.1` : landing page webinaire avec visuels, programme, fiche participant et CTA WhatsApp.

## Sources

Documents de cadrage :

- `guide_nouveaux_comportemant.docx`
- `document_technique_depot_LN_IA_SC.docx`
- `guide_orchestration_LN_IA_SC.docx`
- `guide_chef_atelier.docx`

Documentation utile :

- GitHub Pages : https://docs.github.com/pages
