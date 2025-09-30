config = {
    'model_params': {
        'input_dim': 10,
        'hidden_dim': 64,
        'num_layers': 2,
        'num_heads': 4,
        'dropout': 0.2,
        'output_dim': 1
    },
    'lr': 0.001,
    'epochs': 50,
    'device': 'cuda' if torch.cuda.is_available() else 'cpu'
}