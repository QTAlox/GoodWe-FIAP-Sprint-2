# EV ChargeOps - Implementacao

Este projeto contem um prototipo em Python para gestao de recargas compartilhadas de veiculos eletricos.

## Executar

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/main.py
```

A API fica disponivel em `http://127.0.0.1:5000`.

## Endpoints

- `GET /` verifica o estado do servico.
- `GET /sessions` retorna as sessoes mockadas.
- `GET /allocation?tarifa=0.85` calcula o custo por usuario.
- `GET /analysis` sinaliza anomalias e agrupa perfis de consumo.

Os dados de exemplo ficam em `data/sessoes.csv`. A integracao SEMS esta representada por um adaptador local; nao ha credenciais ou chamadas externas configuradas.