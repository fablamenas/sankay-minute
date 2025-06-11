# Sankay Minute

Ce dépôt contient un exemple minimal d'interface web permettant de générer dynamiquement un diagramme de Sankey à l'aide de [Plotly](https://plotly.com/javascript/sankey-diagrams/). Le fichier `sankay-minute-configurable.html` propose quelques champs de saisie pour personnaliser les libellés, les valeurs et les couleurs des différentes branches.  Une seconde page permet d'afficher automatiquement un diagramme à partir d'un fichier JSON généré depuis Excel.

> **Note**
> Le dépôt ne fournit plus de fichier Excel d'exemple (`sample_data.xlsx`).
> Pour tester le script de conversion, utilisez votre propre classeur ou préparez un petit fichier CSV que vous convertirez ensuite en Excel.

## Fichiers principaux

- **sankay-minute-configurable.html** : page HTML autonome incluant un script JavaScript pour saisir manuellement quelques valeurs de test puis mettre à jour le graphe via `Plotly.react()`.
- **sankey-from-json.html** : page HTML qui charge automatiquement un fichier `data.json` (généré depuis Excel) et affiche le diagramme.

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

1. Ouvrir `sankay-minute-configurable.html` dans un navigateur moderne.
2. Modifier les libellés, pourcentages et couleurs selon vos besoins.
3. Cliquer sur **Mettre à jour le diagramme** pour rafraîchir la visualisation.
4. Pour afficher vos propres données, générez un `data.json` à partir d'un fichier Excel puis ouvrez `sankey-from-json.html` (idéalement via `python -m http.server`).

Cette page peut servir de base pour créer rapidement des schémas de flux personnalisés.

## Conversion depuis Excel

Un script Python est fourni pour transformer un tableau Excel en fichier JSON compatible avec Plotly. Aucun classeur d'exemple n'est conservé dans le dépôt : utilisez votre propre fichier ou convertissez un petit CSV de test en Excel avant d'exécuter le script.

```bash
python scripts/convert_excel_to_sankey.py mon_tableau.xlsx
```

Cela génère un fichier `data.json` que vous pouvez ensuite afficher avec la page `sankey-from-json.html`. Servez les fichiers via un petit serveur local (`python -m http.server`) pour permettre le chargement du JSON.

## Notes

Le fichier initial a été généré à l'aide de ChatGPT, tout comme cette description.
