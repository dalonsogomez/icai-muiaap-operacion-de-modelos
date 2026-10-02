# Semana 01 · Puesta a punto

Comprobado el 2 de octubre de 2026 en macOS `arm64`:

| Requisito | Evidencia |
| --- | --- |
| `uv` y Python 3.12 | `uv 0.12.9`; `uv run --no-project --python 3.12 python --version` devuelve `Python 3.12.13`. |
| Git e identidad | `git version 2.56.0`; nombre y correo configurados localmente, sin publicarlos aquí. |
| GitHub y repositorio | `git ls-remote` accede al fork `dalonsogomez/icai-muiaap-operacion-de-modelos`. |
| Databricks Free Edition | Workspace y Git Folder del repositorio visibles en la pestaña del navegador. |
| Dataset | `semana1/data/raw/WineQT.csv` existe y el smoke test local lo procesa. |
| Editor y notebooks | VS Code instalado. Su CLI no lista las extensiones Python/Jupyter; queda pendiente confirmar soporte de notebooks en la aplicación. |
| `curl` y Postman | `curl 8.7.1` devuelve 200 para `https://postman-echo.com/get`; Postman Desktop instalado, pero su petición GET queda pendiente de comprobar en la aplicación. |
| Docker y Compose | CLI Docker `29.4.0` y Compose `v5.1.4` disponibles. El daemon no está activo (`docker.sock` no existe): estado pendiente y no bloqueante para S1. |

La ejecución actual en Databricks debe comprobarse con los runs del lote usado para
la entrega. La existencia de la pestaña no demuestra por sí sola que compute,
Registry y API local se hayan ejecutado en ese lote. Para cerrar S1.1 faltan
la comprobación de lectura del CSV con serverless y el GET desde Postman; no
hay error de ejecución registrado para esas dos pruebas.
