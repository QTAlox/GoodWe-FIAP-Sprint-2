# src/ai_module.py
import pandas as pd
from sklearn.ensemble import IsolationForest

def analisar_anomalias(df_sessoes):
    print("🧠 [IA] A executar Isolation Forest para detetar anomalias...")
    df_analise = df_sessoes.copy()
    
    # Configuração do modelo de IA (Assume que 5% dos dados podem ser anomalias)
    modelo = IsolationForest(contamination=0.05, random_state=42)
    
    # Extrai as características relevantes para a IA analisar
    features = df_analise[['duration_hours', 'kwh_consumed']]
    
    # O modelo retorna -1 para anomalias e 1 para sessões normais
    df_analise['anomalia'] = modelo.fit_predict(features)
    
    # Filtra apenas os casos suspeitos
    anomalias = df_analise[df_analise['anomalia'] == -1]
    
    if not anomalias.empty:
        print(f"⚠️️ ATENÇÃO! A IA detetou {len(anomalias)} sessão(ões) com comportamento suspeito (possível fraude ou falha).")
    else:
        print("✅ Padrões de consumo normais verificados pela IA.")
        
    return anomalias