# Respuestas

1. ¿Qué campo identifica la muestra?

    ~> El campo que identifica cada muestra es `sample_id`. Por ejemplo, `red-001` identifica de forma única la primera muestra. Este campo sirve para relacionar la predicción con la muestra original, pero no se utiliza como característica del modelo.

2. ¿Qué once campos consume el modelo?

    ~> El modelo consume estos once campos numéricos:

    - `fixed_acidity`
    - `volatile_acidity`
    - `citric_acid`
    - `residual_sugar`
    - `chlorides`
    - `free_sulfur_dioxide`
    - `total_sulfur_dioxide`
    - `density`
    - `ph`
    - `sulphates`
    - `alcohol`

   Son las mediciones físico-químicas del vino. `sample_id` no se incluye porque solo identifica la muestra y no aporta información para realizar la predicción.

3. Proponed una nueva columna que el contrato debería
rechazar.

    ~> Una columna que el contrato debería rechazar es `quality`. Esta columna contiene la calidad real del vino y sería la variable objetivo, no un dato disponible durante la inferencia. Además, el contrato solo permite las once características esperadas y rechaza las columnas adicionales.

4. Proponed dos valores inválidos y explicad por qué.

    ~> Dos valores inválidos serían:

   - `ph = 1.0`: debe rechazarse porque el contrato establece que el pH debe estar entre `2.5` y `4.5`.
   - `alcohol = 25.0`: debe rechazarse porque el porcentaje de alcohol permitido está entre `5` y `20`.

   En ambos casos, el problema no es el formato del valor, ya que son números, sino que están fuera de los límites definidos por el contrato de entrada. Rechazarlos evita enviar al modelo datos que no cumplen las condiciones esperadas.
