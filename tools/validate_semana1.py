"""Comprobaciones estructurales de la entrega de semana 1, sin Databricks."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WEEK = ROOT / "semana1"
MODULE = WEEK / "modules/01-mlflow-databricks-foundations"


def main() -> None:
    assert (WEEK / "data/raw/WineQT.csv").is_file()
    readmes = sorted(WEEK.rglob("README.md"))
    assert len(readmes) == 7, f"Se esperaban 7 README.md, hay {len(readmes)}"

    notebooks = sorted(MODULE.glob("notebooks/*.ipynb"))
    assert len(notebooks) == 4, f"Se esperaban 4 notebooks, hay {len(notebooks)}"
    for path in notebooks:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        assert notebook["nbformat"] == 4
        assert notebook["cells"], f"Notebook vacío: {path}"
        student_notebook = not path.stem.endswith("_solucion")
        visible_outputs = 0
        sources = []
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code":
                source = "".join(cell["source"])
                sources.append(source)
                assert "NotImplementedError" not in source, f"Celda incompleta: {path}"
                if student_notebook:
                    assert cell.get("execution_count") is not None, f"Celda sin ejecutar: {path}"
                    outputs = cell.get("outputs", [])
                    visible_outputs += bool(outputs)
                    assert all(output["output_type"] != "error" for output in outputs), f"Error en salida: {path}"
        if student_notebook:
            assert visible_outputs > 0, f"Notebook sin salidas visibles: {path}"
        if path.name == "01_tracking_mlops.ipynb":
            assert not any("X_test.head(" in source for source in sources), (
                "Los smoke tests deben usar validación; X_test queda reservado para el ganador."
            )
    print(f"Semana 1: {len(readmes)} README, {len(notebooks)} notebooks JSON válidos y dataset presente")


if __name__ == "__main__":
    main()
