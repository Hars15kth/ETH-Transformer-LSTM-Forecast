import torch
import torch.nn as nn

class MultiHeadLSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, dropout):
        super().__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True, dropout=dropout)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.dropout(out)

class TransformerBlock(nn.Module):
    def __init__(self, hidden_dim, num_heads, dropout):
        super().__init__()
        self.attn = nn.MultiheadAttention(hidden_dim, num_heads, dropout=dropout, batch_first=True)
        self.norm = nn.LayerNorm(hidden_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        attn_out, _ = self.attn(x, x, x)
        x = self.norm(x + self.dropout(attn_out))
        return x

class ForecastModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, num_heads, dropout, output_dim):
        super().__init__()
        self.encoder = MultiHeadLSTM(input_dim, hidden_dim, num_layers, dropout)
        self.transformer = TransformerBlock(hidden_dim, num_heads, dropout)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.encoder(x)
        x = self.transformer(x)
        return self.fc(x[:, -1])