# Release GitHub - v0.2.19

## Titre

LN-IA Studio Coachs v0.2.19 - Présentations laboratoire et landing page optimisée

## Résumé

Cette release enrichit le projet avec deux nouvelles présentations PowerPoint :

- une adaptation LN-IA Studio Coachs de la présentation `presentation-lab-num-ctm.pptx` ;
- une présentation spécifique pour la partie pratique sur l'optimisation de landing page.

Elle ajoute aussi une analyse textuelle du PPTX source afin de garder une trace du fil narratif utilisé pour l'adaptation.

## Fichiers ajoutés

- `docs/presentation/presentation-lab-num-ctm.pptx`
- `docs/presentation/analyse-presentation-lab-num-ctm.md`
- `docs/presentation/ln-ia-studio-coachs-lab-numerique-adapte.pptx`
- `docs/presentation/ln-ia-atelier-landing-page-optimisee.pptx`
- `scripts/generate-ln-ia-additional-presentations.py`

## Présentation adaptée

La présentation adaptée reprend la logique du fichier source :

- pourquoi maintenant ;
- c'est quoi ;
- pour qui ;
- comment ;
- challenge et prochaine étape.

Elle déplace le contenu vers l'activité LN-IA Studio Coachs : coaching augmenté par IA, facilitation, production de supports, kit atelier, GitHub, releases et communauté.

## Présentation pratique

La présentation landing page optimisée couvre :

- contexte de la landing page LN-IA ;
- objectifs d'optimisation ;
- grille d'analyse ;
- prompt maître ;
- exercice participant ;
- critères qualité ;
- publication et release GitHub.

## Design

Le design a été renforcé avec plusieurs types de layouts afin d'éviter une présentation monotone :

- slides de titre sombres ;
- slides à cartes ;
- slides processus ;
- comparaison avant/après ;
- timeline du challenge 100 jours ;
- slides avec visuels intégrés.

## Vérifications

- `ln-ia-studio-coachs-lab-numerique-adapte.pptx` : 21 slides, 2 médias.
- `ln-ia-atelier-landing-page-optimisee.pptx` : 14 slides, 3 médias.
- Les fichiers sont générés par un script reproductible.
- Le design combine slides de titre, cartes, processus, comparaison avant/après, timeline et slides avec visuels.

## Commande de régénération

```bash
py scripts/generate-ln-ia-additional-presentations.py
```
