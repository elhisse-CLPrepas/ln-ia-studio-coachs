# Process Zoom IA - LN-IA

## Intention

Ce document définit un protocole de maîtrise pour utiliser Zoom comme salle de formation augmentée dans le projet **LN-IA - Laboratoire Numérique Intelligence Artificielle**.

L'objectif n'est pas seulement de faire un webinaire. L'objectif est d'orchestrer tout le cycle :

1. préparer ;
2. animer ;
3. capter ;
4. transformer ;
5. versionner ;
6. améliorer.

## Positionnement

Zoom devient un espace pédagogique augmenté :

- salle de webinaire ;
- outil de captation ;
- espace d'interaction ;
- source de traces ;
- point de départ de supports ;
- matière première pour l'amélioration continue.

LN-IA transforme ces traces en livrables pédagogiques, supports d'atelier, FAQ, offres et prochaines versions.

## Question centrale

Comment relier Zoom, l'IA, GitHub et les supports pédagogiques pour créer un système d'apprentissage moderne, traçable et améliorable ?

## Réponse courte

Oui, Zoom peut être relié à GitHub, mais il faut distinguer trois niveaux :

1. **Niveau simple** : utiliser Zoom et AI Companion pour capter, résumer et structurer les webinaires.
2. **Niveau projet** : transformer les traces Zoom en fichiers versionnés dans GitHub.
3. **Niveau avancé** : utiliser les intégrations Zoom Marketplace, GitHub Notifications, Zoom API ou Zoom AI Studio selon les droits et licences.

Pour LN-IA, le bon départ est le niveau 1 puis le niveau 2.

## Niveau 1 - Zoom comme salle augmentée

### Avant la session

Préparer :

- la landing page ;
- le conducteur 2h ;
- le script d'animation ;
- le skill d'optimisation ;
- les prompts ;
- la fiche de collecte des besoins ;
- le lien WhatsApp ;
- le lien Zoom ;
- les visuels.

Vérifier dans Zoom :

- micro ;
- caméra ;
- partage écran ;
- chat ;
- enregistrement cloud ;
- paramètres AI Companion si disponibles ;
- résumé de réunion si disponible ;
- transcription ou sous-titres si disponibles.

### Pendant la session

Utiliser Zoom pour :

- présenter ;
- partager la landing page ;
- tester le skill ;
- capter les questions ;
- faire réagir le public ;
- enregistrer ;
- produire une trace.

Rôle de l'animateur :

- garder la vision ;
- reformuler les questions ;
- noter les besoins ;
- relier les échanges aux solutions LN-IA ;
- annoncer les suites.

### Après la session

Récupérer :

- enregistrement ;
- résumé ;
- transcription ;
- chat ;
- questions ;
- actions à suivre ;
- réactions du public.

Transformer ces éléments en :

- compte-rendu post-atelier ;
- FAQ ;
- supports participant ;
- nouveaux prompts ;
- prochaine offre ;
- nouvelles tâches GitHub.

## Niveau 2 - GitHub comme mémoire de progression

GitHub sert à versionner ce qui est produit après Zoom.

Après chaque webinaire :

1. Créer ou mettre à jour les fichiers dans `docs/atelier/`.
2. Ajouter les questions du public.
3. Mettre à jour la FAQ.
4. Mettre à jour les messages de partage.
5. Mettre à jour `CHANGELOG.md`.
6. Faire un commit.
7. Créer un tag si la version est significative.
8. Pousser vers GitHub.

Exemple :

```bash
git status
git add docs/atelier CHANGELOG.md README.md
git commit -m "Add post-webinar insights"
git tag v0.2.9
git push origin main
git push origin v0.2.9
```

## Niveau 3 - Connexion Zoom et GitHub

### Connexion simple existante

Zoom propose une app **GitHub Notifications** pour recevoir dans Zoom Chat des notifications liées aux dépôts GitHub.

Usage possible :

- recevoir des notifications de commits ;
- suivre les changements du dépôt ;
- informer une équipe ;
- garder le lien entre production GitHub et communication Zoom.

### Connexion avancée

Selon les licences et droits disponibles, Zoom peut aussi s'intégrer à des outils avancés :

- Zoom App Marketplace ;
- Zoom API ;
- Zoom AI Companion ;
- Zoom AI Companion on the web ;
- Zoom Virtual Agent / AI Studio ;
- intégrations tierces.

Ces options demandent souvent :

- compte Zoom adapté ;
- droits administrateur ;
- pré-approbation d'app ;
- connexion GitHub ;
- configuration de sécurité ;
- vérification des permissions.

## Recommandation LN-IA

Ne pas commencer par l'intégration technique complexe.

Commencer par un protocole pédagogique solide :

1. Zoom capte la session.
2. LN-IA extrait les besoins.
3. Oria aide à transformer les traces.
4. GitHub versionne les livrables.
5. La formation s'améliore à chaque cycle.

## Process opérationnel LN-IA

### Étape 1 - Préparer

- Choisir le thème.
- Mettre à jour la landing page.
- Préparer les supports.
- Préparer les prompts.
- Préparer le skill.
- Préparer les questions de discussion.

### Étape 2 - Animer

- Présenter la vision.
- Montrer le skill.
- Tester en direct.
- Faire participer.
- Recueillir les besoins.

### Étape 3 - Capter

- Enregistrer.
- Sauvegarder le chat.
- Récupérer le résumé.
- Récupérer les questions.
- Noter les décisions.

### Étape 4 - Transformer

- Produire un compte-rendu.
- Mettre à jour la FAQ.
- Créer une fiche de besoins.
- Améliorer les supports.
- Créer une nouvelle offre si besoin.

### Étape 5 - Versionner

- Commit Git.
- Tag de version.
- Push GitHub.
- Mise à jour du changelog.

### Étape 6 - Améliorer

- Identifier les répétitions.
- Identifier les questions fortes.
- Créer un nouveau skill.
- Préparer un nouvel atelier.

## Tableau de pilotage

| Moment | Zoom | LN-IA | GitHub |
|---|---|---|---|
| Avant | lien, réglages, AI Companion | supports, prompts, skill | fichiers prêts |
| Pendant | webinaire, chat, enregistrement | animation, collecte, reformulation | pas d'action nécessaire |
| Après | résumé, transcript, enregistrement | synthèse, FAQ, supports | commit, tag, push |

## Rôle d'Oria

Oria accompagne le processus :

- structurer les idées ;
- préparer les supports ;
- relire les textes ;
- transformer les traces Zoom ;
- produire des fiches ;
- préparer les commits ;
- garder la cohérence de la formation ;
- aider à documenter l'apprentissage.

## Points de vigilance

- Vérifier les paramètres de confidentialité Zoom.
- Informer les participants si l'enregistrement est activé.
- Vérifier les limites des résumés IA.
- Relire tout contenu généré par IA.
- Ne pas publier de données personnelles sans accord.
- Garder un cadre humain, éthique et pédagogique.

## Sources officielles utiles

- Zoom AI Companion : https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057623
- Données et AI Companion : https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057861
- Meeting Summary : https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0058013
- Smart Recording : https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0058511
- Zoom GitHub Notifications : https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067830
- Zoom App Marketplace : https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0062865
