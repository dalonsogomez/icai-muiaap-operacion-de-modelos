# Semana 01 · Puesta a punto

Comprobado el 2 de octubre de 2026 en macOS `arm64`:

| Requisito | Evidencia |
| --- | --- |
| `uv` y Python 3.12 | `uv 0.12.9`; `uv run --no-project --python 3.12 python --version` devuelve `Python 3.12.13`. |
| Git e identidad | `git version 2.56.0`; nombre y correo configurados localmente, sin publicarlos aquí. |
| GitHub y repositorio | `git ls-remote` accede al fork `dalonsogomez/icai-muiaap-operacion-de-modelos`. |
| Databricks Free Edition | Git Folder de `tareas-semana1` y compute serverless comprobados mediante la ejecución completa de los notebooks; lote de tracking `bd8c6a4c`. |
| Dataset | `semana1/data/raw/WineQT.csv` fue leído por el notebook en serverless y produjo siete runs; también existe en el checkout y pasa el smoke test local. |
| Editor y notebooks | Visual Studio Code 1.140.0 abre `01_tracking_mlops.ipynb` como notebook; extensiones `ms-python.python` y `ms-toolsai.jupyter` instaladas. |
| `curl` y Postman | `curl 8.7.1` devuelve 200 para `https://postman-echo.com/get`; Postman Desktop 12.29.2 devolvió `200 OK` para `GET https://postman-echo.com/get` (137 ms). |
| Docker y Compose | CLI Docker `29.4.0` y Compose `v5.1.4` disponibles. El daemon no está activo (`docker.sock` no existe): estado pendiente y no bloqueante para S1. |

Los IDs del lote, Registry y API están en `02_evidencia_databricks.md`. El
servidor HTTP de la práctica vive dentro del driver de Databricks: el GET de
Postman comprueba el cliente de escritorio con el servicio Echo, no pretende
acceder desde este Mac al `127.0.0.1` del driver remoto. Docker sigue pendiente
de levantar su daemon; el assignment 1.1 lo declara no bloqueante.
