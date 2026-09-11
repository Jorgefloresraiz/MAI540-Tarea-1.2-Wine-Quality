# Wine Quality — Descripción de datos

Fuente original: UCI Machine Learning Repository — Wine Quality Dataset
(Cortez, Cerdeira, Almeida, Matos & Reis, 2009). Vinos "Vinho Verde" portugueses.

- Filas: 6,497 (1,599 tinto + 4,898 blanco), combinados en un solo archivo con la columna `wine_type`.
- Variable objetivo: `quality` (entero de 3 a 9, puntuación sensorial mediana de al menos 3 catadores)
- Clases desbalanceadas: la mayoría de los vinos tienen `quality` 5, 6 o 7; hay muy pocos en los extremos (3, 4, 8, 9).

## Columnas

| Columna | Tipo | Descripción |
|---|---|---|
| wine_type | categórica | `red` o `white` |
| fixed acidity | numérica | Acidez fija |
| volatile acidity | numérica | Acidez volátil |
| citric acid | numérica | Ácido cítrico |
| residual sugar | numérica | Azúcar residual |
| chlorides | numérica | Cloruros |
| free sulfur dioxide | numérica | Dióxido de azufre libre |
| total sulfur dioxide | numérica | Dióxido de azufre total |
| density | numérica | Densidad |
| pH | numérica | pH |
| sulphates | numérica | Sulfatos |
| alcohol | numérica | Grado alcohólico |
| quality | numérica (objetivo) | Puntuación de calidad, 3 a 9 |

No hay valores faltantes en este dataset.

## Nota sobre esta versión académica
El archivo `datos.csv` fue ajustado únicamente en cantidad de registros para mantener una carga de trabajo comparable entre las variantes de la tarea. Las variables, la variable objetivo y el alcance indicado en `README.md` se mantienen sin cambios.
