# Plantilla de bitácora de desarrollo asistido

> Extensión sugerida: 1–2 páginas. Redacta con tus propias palabras.

## 1. Comprensión inicial
El proyecto busca predecir en la calidad del vino mediante un modelo de regresión, utilizando características físico, químicas. El conjunto de datos contienen 6497, observaciones de vinos, tintos y también vinos blancos, y la variable objetivo es calidad, que representa la puntuación de calidad asignada al vino.

En su estado inicial, el proyecto utiliza un modelo de regresión lineal con cuatro variables predictoras: alcohol, volatile acidity, sulphates y density. Al ejecutar el proyecto confirme que el modelo funcionaba, pero estaba deliberadamente limitado. La mejora pendiente consistía en ampliar el modelo a los 10 predictores establecidos en el Readme, incorporar wine_type cómo variable categóricas y añadir el preprocesamiento requerido mediante ColumnTransformer. 

## 2. Ejecución inicial (ANTES)
Ejecute el proyecto original desde la terminal utilizando el comando “Python main.py”. El programa se ejecutó correctamente, sin presentar errores puntos.

El conjunto de datos utilizado contenía 6,497 observaciones y el modelo inicial empleaba cuatro predictores:  alcohol, volatile acidity, sulphates y density. Utilizando una división de datos con “test_size=0.25 y random_state=42, obtuve los siguientes resultados, como punto de referencia:

-MAE: 0.5805
-RMSE: 0.7454
-R²: 0.2522

Estos resultados fueron conservados como evidencia del estado inicial del proyecto y posteriormente utilizados para comparar objetivamente el desempeño del modelo después de implementar la mejora.

## 3. Interacción con Claude Code
Mi objetivo fue completar la mejora del modelo, siguiendo los requisitos establecidos en el “Readme” pero manteniendo control sobre los cambios realizados por Cloud Code. Primero le solicité que examinar el proyecto y sus requisitos antes de realizar modificaciones.

Para evaluar cómo la calidad de una instrucción, afectar al desarrollo asistido por IA, realicé dos experimentos partiendo del mismo proyecto original. En el primero utilicé una instrucción vaga: “ mejora este modelo”. En el segundo proporcione, una instrucción específica que definía lo objetivo, los 10 predictores requeridos, el tratamiento de las variables numéricas y categóricas, el uso de ColumnTransformer y LinearRegression, las métricas requeridas y las restricciones del proyecto.

Antes de permitir modificaciones, en el segundo experimento, solicité a Claude Code un plan de implementación. Claude propuso ampliar el modelo de 4 a 10 predictores, utilizar nuevas variables, numéricas y wine_type como variables categóricas, crear las dos ramas de preprocesamiento y mantener LinearRegression como algoritmo final. Revise el plan y autorice la implementación. Solamente después de confirmar que respetaba los requisitos del Readme. 

Claude Code tomo decisiones operativas relacionadas con la modificación del código y la construcción del Pipeline, mientras que yo mantuve la responsabilidad de revisar el plan, autorizar los cambios, ejecutar la verificaciones y comparar los resultados obtenidos.

## 4. Verificación
Para comprobar los cambios ejecuté nuevamente el proyecto con `python3 main.py` y confirmé que el modelo mejorado funcionaba sin errores. Inspeccioné los cambios realizados en main.py y verifiqué que se utilizaran exactamente los 10 predictores establecidos en el README.md, incluyendo nueve variables numéricas y wine_type como variable categórica.

También verifiqué que el preprocesamiento estuviera integrado mediante ColumnTransformer, utilizando SimpleImputer(strategy="median") y StandardScaler para las variables numéricas, y SimpleImputer(strategy="most_frequent") y OneHotEncoder(handle_unknown="ignore") para la variable categórica. La división de los datos se mantuvo en test_size=0.25 y random_state=42 para conservar la comparabilidad entre ambas ejecuciones.

Como evidencia adicional, utilicé Git para conservar el proyecto original y los dos experimentos en ramas separadas: main, experimento-vago y experimento-especifico. Esto me permitió confirmar que ambos experimentos partieron del mismo baseline y comparar los cambios sin alterar el punto de partida.

## 5. Resultado (DESPUÉS)
espués de implementar la mejora, el modelo utilizó los 10 predictores requeridos y se ejecutó correctamente. Las métricas obtenidas fueron:

- MAE: 0.5712
- RMSE: 0.7375
- R²: 0.2680

En comparación con el punto de partida, el MAE disminuyó de 0.5805 a 0.5712, aproximadamente un 1.6 %, y el RMSE disminuyó de 0.7454 a 0.7375, aproximadamente un 1.1 %. El R² aumentó de 0.2522 a 0.2680, equivalente a una mejora aproximada de 6.3 %.

Los resultados muestran una mejora modesta pero consistente en las tres métricas. El modelo redujo sus errores de predicción y aumentó ligeramente la proporción de variabilidad de la calidad del vino que puede explicar. Además del cambio en las métricas, la nueva implementación cumple con los requisitos establecidos para el tratamiento estructurado de variables numéricas y categóricas.

## 6. Explicación propia
A través de la modificación se logró ampliar el modelo original de cuatro a 10 variables predictoras qué buscan utilizar más información disponible sobre las características del vino. Son un total de nueve de estas variables, las que contienen información numérica, wine_type es la que logra identificar o categorizar si el vino es tinto o blanco y por lo tanto estas requiere un proceso diferente.

A través de la implementación y uso de ColumTransformer se logró separar estos dos tipos de información y aplicar a cada uno de estos el pre procesamiento correspondiente. Dentro de las variables numéricas se implementó el uso de SimpleImputer para lograr manejar los posibles valores ausentes y StandardScaler se estableció para colocar las características en una escala estandarizada. En Wine_type se utiliza OneHotEncoder para transformar las categorías, Red y White para una representación que el modelo pueda procesar de manera certera. 

Luego del pre procesamiento, estos resultados son utilizados por regresión lineal para estimar la variable “quality”. El modelo se evalúa con MAE, RMSE y R².  MAE como el tamaño promedio de el error, dentro de las predicciones y RMSE ciertamente como una medida del error, que penaliza con mayor intensidad los distintos grandes errores. R² indica cuánto de la variación observada en la calidad puede explicar el modelo. 

En comparación entre el estado inicial y el modelo modificado me permitió verificar y corroborar que agregar más variables. No debe asumirse de manera automática como una mejora. Ciertamente el resultado debe ejecutarse, medirse y compararse. En esta situación, las tres métricas, mostraron una mejora importante. Para mí, de hecho verificación, fue una parte esencial del proceso, ya que me permitió evaluar con evidencia el código generado con asistencia de la inteligencia artificial. En lugar de asumir que una modificación técnica más compleja, necesariamente produciría una drástica mejora del resultado.
