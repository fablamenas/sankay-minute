# Sankay Minute

Ce dépôt contient un exemple minimal d'interface web permettant de générer dynamiquement un diagramme de Sankey à l'aide de [Plotly](https://plotly.com/javascript/sankey-diagrams/). Le fichier `sankay-minute-configurable.html` propose quelques champs de saisie pour personnaliser les libellés, les valeurs et les couleurs des différentes branches.

## Fichier principal

- **sankay-minute-configurable.html** : page HTML autonome incluant un script JavaScript pour afficher un diagramme de Sankey. Les données sont lues dans les champs du formulaire puis utilisées pour mettre à jour le graphe via `Plotly.react()`.

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

Cette page peut servir de base pour créer rapidement des schémas de flux personnalisés.

## Notes

Le fichier initial a été généré à l'aide de ChatGPT, tout comme cette description.
