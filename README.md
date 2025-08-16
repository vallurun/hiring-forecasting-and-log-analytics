# Hiring Forecasting & Log Analytics

Simulates **real-time application logs** and builds a **daily hiring forecast**. Uses PySpark for streaming/batch transforms and scikit-learn for simple forecasting. Can be adapted to AWS Kinesis/EMR.

## Components
- **Stream**: `producer.py` appends JSONL logs to `data_samples/stream_logs/`.
- **Consumer**: `consumer_spark.py` tails folder (as a Kinesis stand-in), aggregates KPIs.
- **Forecast**: `train_forecast.py` trains a model; `score_forecast.py` generates future demand.

## Commands to Push
```bash
git init && git add .
git commit -m "init: hiring forecasting & log analytics"
git branch -M main
git remote add origin https://github.com/<your-user>/hiring-forecasting-and-log-analytics.git
git push -u origin main
```
