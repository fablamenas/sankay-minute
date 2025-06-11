import argparse
import json
from pathlib import Path

import pandas as pd


def excel_to_sankey(path: str) -> dict:
    """Convertit un fichier Excel en dictionnaire compatible avec Plotly Sankey."""
    df = pd.read_excel(path)
    df = df.rename(columns={c: c.lower() for c in df.columns})

    required = {"source", "target", "value"}
    if not required.issubset(df.columns):
        raise ValueError(
            f"Les colonnes requises {required} sont absentes du fichier {path}"
        )

    labels = pd.unique(df[["source", "target"]].values.ravel())
    label_index = {label: i for i, label in enumerate(labels)}

    sources = df["source"].map(label_index).astype(int).tolist()
    targets = df["target"].map(label_index).astype(int).tolist()
    values = df["value"].astype(float).tolist()

    data = {
        "node": {"label": labels.tolist()},
        "link": {"source": sources, "target": targets, "value": values},
    }
    return data


def main():
    parser = argparse.ArgumentParser(
        description="Convertit un tableau Excel en fichier JSON pour un diagramme Sankey"
    )
    parser.add_argument("excel_file", help="Chemin du fichier Excel contenant les colonnes source, target et value")
    parser.add_argument(
        "-o",
        "--output",
        default="docs/data.json",
        help="Nom du fichier JSON de sortie (par d\u00e9faut docs/data.json)",
    )
    args = parser.parse_args()

    data = excel_to_sankey(args.excel_file)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Fichier {args.output} g\u00e9n\u00e9r\u00e9 avec succ\u00e8s")


if __name__ == "__main__":
    main()
