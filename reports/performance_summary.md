\# 📊 Performance Summary



This report summarizes forecasting performance across multiple models and aggregation strategies for Ethereum token transfer volumes and volatility metrics.



---



\## 🔹 LSTM Forecasting



\*\*Metrics on 2025 Validation Data:\*\*

\- RMSE: \*e.g.,\* 0.0421  

\- MAE: \*e.g.,\* 0.0317  

\- HR@10: \*e.g.,\* 0.84  

\- NDCG@10: \*e.g.,\* 0.79  



\*\*Visuals:\*\*

\- Calibration plot  

\- Residuals  

\- Forecast vs Actual  

\- Panel forecast (2026)



---



\## 🔹 Transformer Forecasting



\*\*Metrics on 2025 Validation Data:\*\*

\- RMSE: \*e.g.,\* 0.0453  

\- MAE: \*e.g.,\* 0.0342  

\- HR@10: \*e.g.,\* 0.81  

\- NDCG@10: \*e.g.,\* 0.76  



\*\*Visuals:\*\*

\- Calibration plot  

\- Residuals  

\- Forecast vs Actual  

\- Panel forecast (2026)



---



\## 🔹 Panel LSTM Aggregation



\*\*2026 Forecast Summary:\*\*

\- Median prediction: stable, centered around zero  

\- Prediction interval: narrow, low uncertainty  

\- Visual: `reports/forecast\_visuals/2026\_panel\_lstm.png`



---



\## 🔹 Panel Transformer Aggregation



\*\*2026 Forecast Summary:\*\*

\- Median prediction: flat, slightly more variance than LSTM  

\- Visual: `reports/forecast\_visuals/2026\_panel\_transformer.png`



---



\## 📁 Visuals Directory



All plots are available in \[`reports/forecast\_visuals/`](forecast\_visuals/)



