# Wine Quality

Proyecto reproducible para entrenar y evaluar un clasificador sobre el dataset
Wine Quality.

## Instalación

Desde la raíz del repositorio:

```bash
cd semana2/wine-quality-project
uv sync --locked
```

## Estructura

```text
data/raw/WineQT.csv
src/wine_quality/train.py
tests/test_train.py
pyproject.toml
uv.lock
```

## Entrenamiento

```bash
uv run --frozen python -m wine_quality.train
```

El entrenamiento muestra el número de filas, variables, clases y el F1 macro
obtenido en validación.

## Tests

```bash
uv run --frozen pytest
```

## Calidad del código

```bash
uv run --frozen ruff check .
```
