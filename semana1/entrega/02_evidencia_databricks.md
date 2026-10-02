# Evidencia observada en Databricks Free Edition

Consulta realizada el 3 de octubre de 2026. Los enlaces llevan al workspace del
alumno y requieren acceso a él. Los identificadores se contrastaron mediante la API de Databricks y las salidas exportadas de los Jobs; las capturas visuales obligatorias del lote actual están pendientes de renovar.

> **Procedencia:** Tracking se ejecutó desde el commit `a5e9a6e` (Job `93662289745255`) y AgentOps desde `d0bdb72` (Job `454297630848090`) en el Git Folder de `tareas-semana1`. Ambos Jobs terminaron con `SUCCESS`; los experimentos conservaron sus IDs y se generaron nuevos runs y trazas.

## Tracking, selección y Registry

- [Experimento `01_tracking_mlops`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs?o=7474651922184125), ID `3572941977725124`.
- Alias usado **en ese lote**: `equipo-01`; `batch.id=0bfa11d4`.
- Candidatos del mismo lote y fase `candidate`:

| Configuración | Run ID |
| --- | --- |
| `extra_trees_300_leaf_1` | [`6800e8b2111149ab8cffc57472c086e3`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/6800e8b2111149ab8cffc57472c086e3?o=7474651922184125) |
| `extra_trees_600_leaf_1` | [`46a52bcee5844a0aa1fd9826f71dc064`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/46a52bcee5844a0aa1fd9826f71dc064?o=7474651922184125) |
| `extra_trees_300_leaf_2` | [`e5c14f6c079849068c9660796d58a8d5`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/e5c14f6c079849068c9660796d58a8d5?o=7474651922184125) |
| `extra_trees_600_leaf_2` | [`85730d1c0c4d4a8299d13e6cd97f966f`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/85730d1c0c4d4a8299d13e6cd97f966f?o=7474651922184125) |
| `extra_trees_300_leaf_3` | [`8d746ffa6dbc45d78b2f4edfcf9c2b4a`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/8d746ffa6dbc45d78b2f4edfcf9c2b4a?o=7474651922184125) |
| `extra_trees_600_leaf_3` | [`6a91d9782a2e4d43b1868ae6c201f8da`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/6a91d9782a2e4d43b1868ae6c201f8da?o=7474651922184125) |
| `xgboost_hist` | [`e549bdc887804c7daf994bf01fd02955`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/e549bdc887804c7daf994bf01fd02955?o=7474651922184125) |

El ganador [`46a52bcee5844a0aa1fd9826f71dc064`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/46a52bcee5844a0aa1fd9826f71dc064?o=7474651922184125) está marcado `selection.status=winner` y `selection.test_used_once=true`.
Su F1 macro de validación es `0.3053074737662099`; la de test, evaluado
después de elegirlo, es `0.32456162551830897`.

En [Catalog Explorer](https://dbc-6a116e70-0ef4.cloud.databricks.com/explore/data/models/workspace/default/wine_quality_classifier_equipo_01?o=7474651922184125), el modelo
`workspace.default.wine_quality_classifier_equipo_01` contiene cuatro versiones históricas; las versiones del lote actual son dos (3 y 4). La versión 3 es la referencia de rollback y la
[versión 4](https://dbc-6a116e70-0ef4.cloud.databricks.com/explore/data/models/workspace/default/wine_quality_classifier_equipo_01/version/4?o=7474651922184125)
procede del run ganador y muestra los alias `@challenger` y `@champion`.

**Captura del filtro del lote nuevo pendiente de renovar.**

**Captura de los siete candidatos del lote nuevo pendiente de renovar.**

**Captura del lote nuevo pendiente de renovar:** la imagen existente corresponde al lote anterior y no acredita las versiones 3 y 4.

## API local de la práctica

El [run de deployment `0e971b10d1094b869f86dc0e08c995de`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/0e971b10d1094b869f86dc0e08c995de?o=7474651922184125)
apunta al ganador del lote actual y a la versión 4. Su
[artefacto `deployment/evidence.json`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725124/runs/0e971b10d1094b869f86dc0e08c995de/artifacts?selectedArtifact=0e971b10d1094b869f86dc0e08c995de%3Adeployment%2Fevidence.json&o=7474651922184125)
registra `GET /health → 200`, predicción válida `→ 200`, contrato incompleto
`→ 400` y JSON que no es objeto `→ 400`. Las métricas del run suman cuatro
peticiones, dos correctas, dos rechazadas y cero errores internos; latencia
media `34.731786500003636 ms` y máxima `138.0100809999476 ms`.

El propio artefacto identifica el servicio como `local_notebook_http`, con
`public_endpoint=false` y `persistent=false`. El artefacto `governance/s01_project_record.yaml` del run de deployment y la salida final del notebook confirman
`api_stopped=true`. La captura acredita las pruebas
registradas, **no** que exista ahora un endpoint público ni que el servidor
efímero siga en funcionamiento.

El artefacto del run y las salidas del notebook acreditan las pruebas del lote nuevo; la imagen anterior se renovará antes de cerrar la entrega.

## AgentOps y evaluación

En el [experimento `02_agent_llmops`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725126?o=7474651922184125)
(ID `3572941977725126`) se han contrastado:

- [Traza OK `tr-42df544991d015f9562647d01febda27`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725126/traces?o=7474651922184125&selectedEvaluationId=tr-42df544991d015f9562647d01febda27): pregunta sobre diagnóstico clínico; respuesta didáctica que rechaza el consejo clínico.
- [Traza ERROR `tr-a777f66c0dce67b2583d65f312aa172b`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725126/traces?o=7474651922184125&selectedEvaluationId=tr-a777f66c0dce67b2583d65f312aa172b): entrada `unknown-topic` y error controlado.
- [Run de evaluación `bc543f9cd83d42e78d7fc4ce50e205b2`](https://dbc-6a116e70-0ef4.cloud.databricks.com/ml/experiments/3572941977725126/evaluation-runs/bc543f9cd83d42e78d7fc4ce50e205b2/details?o=7474651922184125): ocho casos; `contains_expected_phrase/mean=1`, `response_is_concise/mean=1` y `safety_refusal/mean=1`.

Son comprobaciones heurísticas sobre un agente determinista, con `USE_LLM=False`.
La puntuación perfecta no demuestra corrección clínica ni seguridad general.

La captura de la traza ERROR del lote anterior no se utiliza como prueba de este lote.

La captura de trazas OK del lote anterior no se utiliza como prueba de este lote.

La captura de evaluación del lote anterior no se utiliza como prueba de este lote; el run se verificó por API.

## Notebooks ejecutados y correspondencia con las guías

Los notebooks conservan las salidas de los Jobs de Databricks, reconstruidas desde el modelo de ejecución de `jobs export-run`, sin reutilizar las salidas de un lote anterior. Se conservaron en sus rutas
originales: [`01_tracking_mlops.ipynb`](../modules/01-mlflow-databricks-foundations/notebooks/01_tracking_mlops.ipynb)
y [`02_agent_llmops.ipynb`](../modules/01-mlflow-databricks-foundations/notebooks/02_agent_llmops.ipynb).
Las 21 celdas de código de Tracking y las 7 de AgentOps tienen `execution_count`. Ninguna tiene una salida de tipo `error`; el `KeyError` de AgentOps fue esperado, capturado y quedó registrado como traza `ERROR`. Las celdas que sólo importan o definen funciones no
producen una salida visible.

| Indicación del ejercicio | Evidencia verificable |
| --- | --- |
| Datos, split estratificado 70/15/15 y siete candidatos con XGBoost | Celdas 9–23 del notebook de tracking; siete runs con `batch.id=0bfa11d4`. |
| Inputs, parámetros, métricas y artefactos por candidato | Run de cada candidato; celdas 19–23. Incluyen `mlflow.log_input`, tarjeta y calidad de datos, riesgos, reporte, matriz, firma, `input_example`, `model.joblib` y contrato. |
| Gate sobre validación y test posterior sólo en el ganador | Celdas 25–29; ganador `46a52bcee5844a0aa1fd9826f71dc064`, F1 macro de validación `0.3053074737662099` y de test `0.32456162551830897`. |
| Registry y ciclo de alias | Celdas 31–33; versiones 3 y 4, `Challenger`, `Champion`, rollback a 3 y re-promoción a 4. |
| API local y run de observabilidad | Celdas 35–45; cuatro respuestas HTTP, contadores `4/2/2/0` y apagado verificado. |
| Trazas anidadas, tags, fallo y ocho evaluaciones | Celdas 6–14 de AgentOps; experimento `3572941977725126`, trazas OK/ERROR y run `bc543f9cd83d42e78d7fc4ce50e205b2`. |

El gate propuesto para una segunda versión es mantener
`safety_refusal/mean = 1.0` en los casos críticos y revisar manualmente sus
respuestas antes de promoverla. Los tres scorers son heurísticos: una frase
puede aparecer negada, la negativa clínica se reconoce por texto fijo y la
longitud no mide veracidad ni utilidad. La ficha YAML recoge esas limitaciones
y el control de evaluación adversarial con revisión humana.
