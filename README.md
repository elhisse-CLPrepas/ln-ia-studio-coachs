# LAB-NUMERIQUE-IA - Studio Coachs

LN-IA-SC est un depot de travail pour preparer, versionner et publier une premiere base de l'atelier **LAB-NUMERIQUE-IA - Studio Coachs**.

Le projet transforme les documents sources sur le coaching augmente par IA en un support web simple, un kit pedagogique initial et une base de production exploitable avec VS Code, Codex, Git et GitHub.

## Intention

Produire un systeme d'apprentissage assiste par IA pour les coachs, formateurs, enseignants et accompagnateurs.

La promesse de depart n'est pas de remplacer le coach par l'IA. Elle consiste a outiller le coach pour mieux observer, formaliser, simuler, produire, transmettre et accompagner l'apprentissage de nouveaux comportements.

## Sources principales

Les documents de reference du projet sont :

- `guide_nouveaux_comportemant.docx` : guide pedagogique source sur l'apprentissage de nouveaux comportements a l'ere du coaching augmente par IA.
- `document_technique_depot_LN_IA_SC.docx` : document technique de depot et de lancement.
- `guide_orchestration_LN_IA_SC.docx` : guide operationnel d'orchestration.
- `guide_chef_atelier.docx` : guide de pilotage pour preparer, lancer et controler le travail avec Codex dans VS Code.

Les copies de travail doivent etre rangees dans `docs/source/`.

## Structure du depot

```text
ln-ia-studio-coachs/
├── README.md
├── BRIEF-CODEX.md
├── ROADMAP.md
├── CHANGELOG.md
├── LICENSE
├── docs/
│   ├── source/
│   └── guide-ln-ia-sc.docx
├── data/
│   ├── flashcards.json
│   ├── faq.json
│   ├── prompts.json
│   └── parcours.json
├── assets/
│   ├── css/
│   ├── js/
│   └── img/
├── share/
└── index.html
```

## Objectif v0.1.0

La version `v0.1.0` doit rester volontairement limitee.

Elle vise a obtenir :

- une structure de depot propre ;
- un README de cadrage ;
- un brief Codex court et executable ;
- une page `index.html` statique minimale ;
- des fichiers de donnees JSON valides ;
- les documents sources et visuels ranges aux bons emplacements ;
- une base prete pour un premier commit et une future release GitHub.

Hors perimetre `v0.1.0` :

- application complexe ;
- back-end ;
- authentification ;
- automatisation avancee ;
- design final ;
- contenus pedagogiques exhaustifs.

## Utilisation locale

Ouvrir directement `index.html` dans un navigateur suffit pour cette premiere version statique.

## Pilotage Codex

La mission active de Codex est de produire uniquement la base `v0.1.0` de LN-IA-SC, sans ajouter de fonctionnalites non demandees. Les consignes detaillees sont dans `BRIEF-CODEX.md`.
