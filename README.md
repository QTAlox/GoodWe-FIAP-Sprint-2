# GoodWe FIAP Challenge: EV ChargeOps

Prototipo para consolidar sessoes de recarga, calcular rateio de custos por usuario e explorar anomalias e perfis de consumo. A integracao com a SEMS esta representada por um adaptador local que le `data/sessoes.csv`; nao ha chamadas externas nem credenciais configuradas.

## Requisitos

- Python 3.10 ou superior
- Dependencias listadas em `requirements.txt`

## Executar no Windows (PowerShell)

A partir desta pasta do projeto:

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
- `GET /allocation?tarifa=0.85` calcula o custo por usuario; a tarifa e expressa em unidade monetaria por kWh.
- `GET /analysis` aplica Isolation Forest para sinalizar anomalias e K-Means para agrupar perfis exploratorios.

## Estrutura

- `data/`: conjunto de sessoes mockadas.
- `src/`: adaptador SEMS, rateio, analise e API Flask.
- `notebooks/`: reservado para analises interativas.
- `docs/`: reservado para arquitetura e evidencias do desafio.

Os resultados de IA sao demonstrativos e devem ser calibrados e avaliados com dados reais antes de uso operacional.
