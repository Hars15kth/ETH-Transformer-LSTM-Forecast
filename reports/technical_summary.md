\##  Technical Summary



This project implements a hybrid deep learning pipeline for forecasting Ethereum token transfer volumes and volatility. It includes:



\### 🔹 Data

\- Raw ERC20 token transfer counts and log-realized variance

\- Time-series split for 2025 validation and 2026 forecasting



\### 🔹 Models

\- \*\*LSTM\*\*: Sequential modeling with dropout and early stopping

\- \*\*Transformer\*\*: Multi-head attention with positional encoding

\- \*\*Panel Aggregation\*\*: Median ensemble across multiple runs



\### 🔹 Metrics

\- RMSE, MAE for regression

\- HR@10, NDCG@10 for ranking-based evaluation



\### 🔹 Visuals

\- Calibration plots, residuals, forecast vs actual

\- 2026 panel-level forecasts for both LSTM and Transformer



\### 🔹 Reproducibility

\- All notebooks and markdown summaries are versioned

\- Forecast visuals and metrics are traceable to source notebooks

\- Licensing restricts reuse and enforces ownership



See \[`reports/performance\_summary.md`](reports/performance\_summary.md) for full metrics and plots.

