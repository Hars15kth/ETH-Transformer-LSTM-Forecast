import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from src.model import ForecastModel
from src.utils import compute_metrics

def train_model(train_loader, val_loader, config):
    model = ForecastModel(**config['model_params']).to(config['device'])
    optimizer = torch.optim.Adam(model.parameters(), lr=config['lr'])
    criterion = nn.MSELoss()

    for epoch in range(config['epochs']):
        model.train()
        for batch in train_loader:
            x, y = batch
            x, y = x.to(config['device']), y.to(config['device'])
            preds = model(x)
            loss = criterion(preds, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            all_preds, all_targets = [], []
            for batch in val_loader:
                x, y = batch
                x, y = x.to(config['device']), y.to(config['device'])
                preds = model(x)
                all_preds.append(preds)
                all_targets.append(y)

        compute_metrics(torch.cat(all_preds), torch.cat(all_targets))