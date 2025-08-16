import pandas as pd
import joblib

hist = pd.read_csv("data_samples/hiring_daily.csv", parse_dates=["date"]).sort_values("date")
model = joblib.load("rf_applies.joblib")

# One-step ahead using last two days
lag1 = hist.iloc[-1]["applies"]
lag2 = hist.iloc[-2]["applies"]
forecast = model.predict([[lag1, lag2]])[0]
print({"next_day_applies_forecast": round(float(forecast))})
