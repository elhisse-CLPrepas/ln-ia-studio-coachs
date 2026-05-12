# Sélection des modèles IA - LN-IA Studio Coachs

Date de cadrage : 12 mai 2026.

Cette fiche choisit les modèles les plus connus et les plus adaptés à l'activité LN-IA Studio Coachs : coaching augmenté, facilitation, production de supports, analyse de documents, optimisation de landing page et animation d'atelier.

## Principe de sélection

Ne pas multiplier les outils pendant l'atelier. Utiliser peu de modèles, mais les utiliser clairement.

La règle LN-IA :

- un modèle principal pour produire ;
- un modèle challenger pour relire et améliorer ;
- un modèle multimodal pour analyser documents, images ou supports ;
- un modèle francophone/open quand le contexte demande plus de souveraineté ou de transparence ;
- un outil de recherche avec sources quand l'information doit être vérifiée.

## Stack recommandée

| Usage | Modèle recommandé | Pourquoi |
|---|---|---|
| Animation, prompts, synthèse, supports pédagogiques | GPT-5.2 / ChatGPT-5.2 | Très adapté au travail professionnel, aux tâches longues, à la structuration, aux présentations, au code et à l'analyse multimodale. |
| Relecture critique, reformulation humaine, éthique, pédagogie | Claude Sonnet 4 ou Claude Opus 4.1 | Très utile pour challenger un texte, améliorer la clarté, détecter les angles morts et garder une tonalité humaine. |
| Analyse de documents longs, PDF, images, vidéo, contexte large | Gemini 2.5 Pro ou Gemini 3 Pro Preview | Pertinent pour les contenus longs, multimodaux, les supports visuels et l'analyse croisée de documents. |
| Production rapide, variantes, brouillons, tâches à volume | GPT-5 mini, Gemini 2.5 Flash ou Gemini 3 Flash Preview | Bon équilibre vitesse/coût pour les variantes de titres, emails, questionnaires, messages de partage et synthèses rapides. |
| Alternative francophone/open, souveraineté, démonstration européenne | Mistral Large 3 ou Mistral Medium 3.5 | Modèles connus, utiles pour ateliers francophones, cas open-weight et besoins de maîtrise plus forte de l'environnement. |
| Code, landing page, automatisation légère | GPT-5.2, GPT-5.2 Codex ou Devstral 2 | Adapté aux améliorations HTML/CSS/JS, aux revues de code et à la production assistée dans VS Code. |
| Transcription et compte-rendu de séance | Whisper / service de transcription Zoom / Voxtral Mini Transcribe | Utile pour transformer la séance en matière exploitable : questions, besoins, décisions, prochaines actions. |

## Choix par défaut pour l'atelier LN-IA

### 1. Modèle principal : GPT-5.2

À utiliser pour :

- préparer le déroulé d'atelier ;
- créer les supports participant ;
- produire les prompts ;
- améliorer la landing page ;
- synthétiser les besoins ;
- générer une note de release ;
- aider dans VS Code avec Codex.

Consigne animateur :

> GPT-5.2 est le modèle de production principal. Il sert à transformer une intention en livrable structuré.

### 2. Modèle challenger : Claude Sonnet 4

À utiliser pour :

- relire un support ;
- détecter les formulations floues ;
- améliorer la posture humaine et pédagogique ;
- vérifier que le message reste clair pour un public non technique ;
- préparer les questions de facilitation.

Consigne animateur :

> Claude sert de second regard. Il ne remplace pas le modèle principal, il l'aide à progresser.

### 3. Modèle multimodal : Gemini 2.5 Pro

À utiliser pour :

- analyser un PDF ou un dossier long ;
- comparer plusieurs supports ;
- lire une image, une affiche, un plan de slides ;
- travailler sur de longs documents de cadrage ;
- préparer une synthèse à partir de sources multiples.

Consigne animateur :

> Gemini est utile quand le support est long, visuel ou composite.

### 4. Modèle francophone/open : Mistral Large 3

À utiliser pour :

- montrer une alternative européenne ;
- travailler en français ;
- discuter souveraineté, open-weight, déploiement et maîtrise ;
- comparer les réponses avec les modèles américains.

Consigne animateur :

> Mistral permet d'ouvrir la discussion sur la souveraineté, le choix des outils et la diversité des modèles.

## Matrice d'usage atelier

| Moment de l'atelier | Modèle conseillé | Production attendue |
|---|---|---|
| Préparation | GPT-5.2 | conducteur, script, objectifs, timing |
| Ouverture | GPT-5.2 + Claude | message clair, posture humaine |
| Vision IA | Gemini ou GPT-5.2 | synthèse pédagogique, exemples |
| Démonstration landing page | GPT-5.2 / Codex | amélioration HTML, structure, CTA |
| Facilitation | Claude Sonnet 4 | questions, reformulations, relances |
| Analyse de besoins | GPT-5.2 + Gemini | typologie des besoins, priorités |
| Compte-rendu | GPT-5.2 ou modèle rapide | synthèse, décisions, prochaines actions |
| Release GitHub | GPT-5.2 / Codex | changelog, commit, tag, release notes |

## Modèles à éviter comme choix par défaut

Éviter comme modèle principal :

- les modèles expérimentaux non stables pour une production officielle ;
- les modèles trop spécialisés si le public découvre l'IA ;
- les modèles sans accès clair aux sources quand l'information doit être vérifiée ;
- les modèles très coûteux pour des tâches simples de reformulation.

Les modèles preview peuvent être montrés en démonstration, mais le kit doit rester utilisable avec des modèles stables.

## Règle de sécurité pédagogique

Pendant l'atelier, rappeler que :

- le modèle propose, l'humain décide ;
- une réponse IA doit être vérifiée avant publication ;
- les données personnelles des participants ne doivent pas être copiées dans un outil sans cadre clair ;
- les sources doivent être citées quand l'information est factuelle ou récente ;
- la qualité vient de l'orchestration : intention, contexte, prompt, production, vérification, amélioration.

## Sources de référence

- OpenAI - GPT-5.2 : https://openai.com/index/introducing-gpt-5-2
- OpenAI API - Using GPT-5.2 : https://platform.openai.com/docs/guides/latest-model
- Anthropic - Claude models overview : https://docs.anthropic.com/en/docs/about-claude/models/overview
- Google AI - Gemini models : https://ai.google.dev/models/gemini
- Google Cloud - Gemini model lifecycle : https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions
- Mistral AI - Models : https://docs.mistral.ai/models
