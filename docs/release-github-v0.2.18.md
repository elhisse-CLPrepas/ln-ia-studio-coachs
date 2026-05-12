# Release GitHub - v0.2.18

## Titre

LN-IA Studio Coachs v0.2.18 - Présentation PowerPoint du webinaire

## Résumé

Cette release ajoute une présentation professionnelle au format `.pptx` pour le webinaire LN-IA Studio Coachs du 12 mai 2026.

La présentation suit le contenu de `docs/atelier/plan-slides-ln-ia-sc.md` et fournit un support clair pour les participants : vision, promesse, New Paradigm IA, skills IA, coach augmenté, atelier pratique, grille d'analyse, exercice et appel à l'action.

## Fichier ajouté

- `docs/presentation/ln-ia-studio-coachs-webinaire-12-mai-2026.pptx`

## Contenu de la présentation

- 12 slides en format 16:9.
- Identité visuelle LN-IA.
- Slides lisibles pour participants.
- Visuels intégrés depuis le projet.
- Support prêt pour le webinaire du 12 mai 2026.

## Génération

Le fichier est généré par :

- `scripts/generate-ln-ia-presentation.py`

Commande :

```bash
py scripts/generate-ln-ia-presentation.py
```

## Vérifications

- Le fichier `.pptx` est présent dans `docs/presentation/`.
- Le package Office contient 12 slides.
- Les médias nécessaires sont embarqués dans le fichier.
