# CONTEXT.md — Wine Quality

## 1. Objetivo y alcance

Este proyecto utiliza aprendizaje automático supervisado mediante regresión para predecir la variable `quality` del conjunto de datos Wine Quality.

El proyecto debe mantener un flujo de trabajo reproducible, verificable y consistente con los requisitos académicos establecidos. Claude Code debe utilizar este archivo como contexto persistente antes de proponer o realizar modificaciones al proyecto.

## 2. Reglas de tratamiento de datos

1. La variable objetivo es `quality`.
2. `quality` está PROHIBIDA como variable predictora. Utilizarla como predictor constituye fuga de información (data leakage).
3. Los datos deben dividirse en entrenamiento y prueba antes de ajustar cualquier transformación que aprenda información de los datos.
4. Las transformaciones deben ajustarse únicamente utilizando los datos de entrenamiento y posteriormente aplicarse a los datos de prueba.
5. Las variables numéricas deben tratarse mediante `SimpleImputer(strategy="median")` y `StandardScaler`.
6. La variable categórica `wine_type` debe tratarse mediante `SimpleImputer(strategy="most_frequent")` y `OneHotEncoder(handle_unknown="ignore")`.
7. No se deben eliminar, modificar o sustituir datos originales sin una justificación explícita.
8. Antes de modificar código, Claude Code debe presentar un plan de los cambios propuestos y esperar autorización.

## 3. Criterios de evaluación

1. El modelo debe evaluarse utilizando MAE, RMSE y R².
2. La división de datos debe mantener `test_size=0.25` y `random_state=42` para permitir comparaciones reproducibles.
3. Los resultados deben compararse con el punto de partida cuando corresponda.
4. Una modificación no debe considerarse una mejora únicamente porque el programa se ejecute sin errores; debe verificarse mediante evidencia y métricas.

## 4. Restricciones del proyecto

1. Mantener `LinearRegression` como algoritmo final salvo que una instrucción académica posterior requiera explícitamente otro algoritmo.
2. No realizar selección automática de características, búsqueda de hiperparámetros, validación cruzada ni ingeniería avanzada de características sin autorización explícita.
3. No modificar la variable objetivo ni redondear las predicciones antes de calcular las métricas.
4. No modificar la estructura de carpetas del proyecto sin autorización.
5. No sobrescribir ni eliminar evidencia necesaria para comparar ejecuciones.

## 5. Seguridad y control humano

1. No incluir credenciales, contraseñas, tokens, claves API ni información confidencial en el código, archivos del proyecto o repositorio.
2. Claude Code debe explicar cualquier operación potencialmente destructiva antes de ejecutarla.
3. Las decisiones propuestas por Claude Code deben ser revisadas por el estudiante antes de autorizar cambios.
4. Si una solicitud contradice una regla de este archivo, Claude Code debe señalar el conflicto y no ejecutar la acción prohibida.
