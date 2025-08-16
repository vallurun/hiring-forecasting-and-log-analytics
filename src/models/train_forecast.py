import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# Load toy daily hiring counts
hist = pd.read_csv("data_samples/hiring_daily.csv", parse_dates=["date"]).sort_values("date")

# Simple features (lags)
hist["applies_lag1"] = hist["applies"].shift(1)
hist["applies_lag2"] = hist["applies"].shift(2)
hist = hist.dropna()

X = hist[["applies_lag1", "applies_lag2"]]
y = hist["applies"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(Xtr, ytr)
pred = model.predict(Xte)

print("R2=", r2_score(yte, pred))
print("MAE=", mean_absolute_error(yte, pred))

joblib.dump(model, "rf_applies.joblib")
print("Saved rf_applies.joblib")
