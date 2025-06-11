# Sankay Minute

Ce dépôt contient un exemple minimal d'interface web permettant de générer dynamiquement un diagramme de Sankey à l'aide de [Plotly](https://plotly.com/javascript/sankey-diagrams/). Les pages HTML sont maintenant regroupées dans le dossier `docs/` afin de pouvoir télécharger le projet et l'utiliser localement avec Jupyter ou un simple navigateur. La page `configurable.html` permet de saisir manuellement quelques valeurs, tandis que `from-json.html` affiche automatiquement un diagramme à partir d'un fichier JSON généré depuis Excel.

## Fichiers principaux

- **docs/configurable.html** : page HTML autonome incluant un script JavaScript pour saisir manuellement quelques valeurs de test puis mettre à jour le graphe via `Plotly.react()`.
- **docs/from-json.html** : page HTML qui permet de charger un fichier `data.json` produit depuis Excel et d'afficher le diagramme.

Extrait du code :
```html
<button onclick="updateDiagram()">Mettre à jour le diagramme</button>
...
function updateDiagram() {
    const labels = [
        document.getElementById("label0").value,
        document.getElementById("label1").value,
        document.getElementById("label2").value,
        document.getElementById("label3").value
    ];
    const values = [
        parseFloat(document.getElementById("val0").value),
        parseFloat(document.getElementById("val1").value),
        parseFloat(document.getElementById("val2").value)
    ];
    const colors = [
        document.getElementById("col0").value,
        document.getElementById("col1").value,
        document.getElementById("col2").value,
        document.getElementById("col3").value
    ];
```

Ces valeurs alimentent ensuite la configuration du diagramme de Sankey.

## Utilisation

1. Ouvrir `docs/index.html` dans un navigateur moderne et choisir la page souhaitée.
2. Dans la page de configuration, modifier les libellés, pourcentages et couleurs selon vos besoins puis cliquer sur **Mettre à jour le diagramme**.
3. Pour afficher vos propres données, générez un `docs/data.json` à partir d'un fichier Excel puis ouvrez la page de chargement du JSON.

Cette page peut servir de base pour créer rapidement des schémas de flux personnalisés.

## Conversion depuis Excel

Un script Python est fourni pour transformer un tableau Excel en fichier JSON compatible avec Plotly.

```bash
python scripts/convert_excel_to_sankey.py mon_tableau.xlsx
```

Cela génère un fichier `docs/data.json` que vous pouvez ensuite ouvrir dans `docs/from-json.html` pour afficher votre diagramme.

## Notes

Le fichier initial a été généré à l'aide de ChatGPT, tout comme cette description.
