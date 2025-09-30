import torch
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def compute_metrics(preds, targets):
    preds = preds.cpu().numpy()
    targets = targets.cpu().numpy()
    rmse = np.sqrt(mean_squared_error(targets, preds))
    mae = mean_absolute_error(targets, preds)
    print(f"RMSE: {rmse:.4f}, MAE: {mae:.4f}")

    # Placeholder for HR@10 and NDCG@10
    # You can plug in your ranking logic here