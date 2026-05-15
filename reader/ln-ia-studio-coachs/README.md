# LN-IA Studio Coachs - Lecteur Web

Projet LN-IA Livre Factory pour transformer un PDF issu d'un PPTX en page de lecture Web.

## Source

- PDF : `sources/ln-ia-studio-coachs-lab-numerique-V1.pdf`
- Pages : 22
- Format : 16:9

## Structure

```text
projects/ln-ia-studio-coachs-reader/
  project_config.json
  build_reader.py
  index.html
  manifest.json
  sources/
  images/
  exports/
```

## Reconstruire les images

Depuis la racine de `ln-ia-livre-factory` :

```powershell
.venv\Scripts\python.exe projects\ln-ia-studio-coachs-reader\build_reader.py
```

Le script convertit chaque page PDF en image JPEG optimisée :

```text
images/page_001.jpg
images/page_002.jpg
...
images/page_022.jpg
```

## Lire localement

Ouvrir directement :

```text
projects/ln-ia-studio-coachs-reader/index.html
```

## Intégrer dans une page existante

Exemple d'intégration par iframe :

```html
<section id="ln-ia-reader" class="ln-ia-reader-section">
  <iframe
    title="Lecteur LN-IA Studio Coachs"
    src="projects/ln-ia-studio-coachs-reader/index.html"
    loading="lazy"
    style="width:100%; min-height:90vh; border:0;"
  ></iframe>
</section>
```

## Déploiement

Le dossier est statique. Il peut être publié tel quel sur GitHub Pages ou copié vers `clprepas.com`.

Point d'entrée :

```text
index.html
```
