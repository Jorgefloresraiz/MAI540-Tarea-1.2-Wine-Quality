from pathlib import Path
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA = Path(__file__).parent / "data" / "datos.csv"

df = pd.read_csv(DATA)

# Punto de partida deliberadamente limitado y comparable con las demás tareas:
# solo usa unas pocas variables sencillas. La mejora completa está en README.md.
features = ['alcohol', 'volatile acidity', 'sulphates', 'density']
X = df[features]
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("model", LinearRegression()),
])
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("=== WINE QUALITY: PUNTO DE PARTIDA ===")
print(f"Filas: {len(df):,}")
print(f"Variables usadas por el modelo inicial: {len(features)}")
mae = mean_absolute_error(y_test, pred)
rmse = mean_squared_error(y_test, pred) ** 0.5
r2 = r2_score(y_test, pred)
print(f"MAE:  {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R2:   {r2:.4f}")
print("\nEl proyecto funciona, pero la mejora equilibrada descrita en README.md todavía no está implementada.")
