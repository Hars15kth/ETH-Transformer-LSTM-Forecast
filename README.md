# Ethereum Forecasting Pipeline

Hybrid deep learning pipeline for forecasting Ethereum token transfer volumes and volatility using LSTM and Transformer architectures. Built for reproducibility, benchmarking, and recruiter-facing presentation.

## Project Overview

This repository showcases a deep learning pipeline for forecasting Ethereum token transfer volumes and volatility using hybrid architectures (LSTM and Transformer). It includes:

- Time-series forecasting on ERC20 transfer counts
- Volatility prediction via log-realized variance modeling
- Model comparison: LSTM vs Transformer vs Panel Aggregation
- Metrics: RMSE, MAE, HR@10, NDCG@10
- Visuals: Calibration plots, residuals, and 2026 panel forecasts

Ethereum Resume Notebook: Demonstrates forecasting pipeline, metrics, and visuals used in the PDF report. Available in [notebooks/Ethereum_resume.ipynb](notebooks/Ethereum_resume.ipynb)

Detailed Technical Summary: [reports/technical_summary.md](reports/technical_summary.md)

Performance Summary: [reports/performance_summary.md](reports/performance_summary.md)

## Repository Structure


ETH-Transformer-LSTM-Forecast/ ├── notebooks/ │   ├── ethereum_forecasting_colab.ipynb │   └── Ethereum_resume.ipynb ├── reports/ │   ├── forecast_visuals/ │   ├── performance_summary.md │   └── technical_summary.md ├── LICENSE.md ├── README.md


## License

This repository is protected under a custom proprietary license.  
No copying, redistribution, or reuse is permitted without explicit written permission.  
Contact: harshwardhansinghx@gmail.com

## Run in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Hars15kth/ETH-Transformer-LSTM-Forecast/blob/main/notebooks/Ethereum_resume.ipynb)


All results are benchmarked and documented in \[`reports/performance\_summary.md`](reports/performance\_summary.md).



📄 Ethereum Resume Notebook: Demonstrates forecasting pipeline, metrics, and visuals used in the PDF report. Available in \[`notebooks/Ethereum\_resume.ipynb`](notebooks/Ethereum\_resume.ipynb)

