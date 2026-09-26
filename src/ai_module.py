import pandas as pd
# TODO: O responsável pela IA deve instalar: pip install scikit-learn
# from sklearn.ensemble import IsolationForest

def analisar_anomalias(df_sessoes):
    """
    Função stub (esqueleto) para detectar anomalias nas recargas.
    
    POR QUE ISSO É ESTRUTURAL? Se um carro consome muito mais que a bateria 
    dele suporta, ou fica conectado 48h sem carregar (ocupando vaga), a IA
    detecta isso e gera um alerta para o síndico/gestor.
    """
    print("🧠 [Módulo de IA] Iniciando análise de anomalias nas sessões...")
    
    # Criamos uma cópia para não alterar os dados originais do rateio
    df_analise = df_sessoes.copy()
    
    # TODO: O membro do grupo focado em IA deve implementar o Isolation Forest aqui.
    # Exemplo rápido do que seria feito:
    # modelo = IsolationForest(contamination=0.1)
    # df_analise['anomalia'] = modelo.fit_predict(df_analise[['duration_hours', 'kwh_consumed']])
    # anomalias = df_analise[df_analise['anomalia'] == -1]
    
    # SIMULAÇÃO DA IA PARA O PROTÓTIPO RODAR SEM ERRO POR ENQUANTO:
    # Vamos considerar "anômalo" quem carregou mais de 35 kWh de uma vez só (simulando a saída da IA)
    anomalias = df_analise[df_analise['kwh_consumed'] > 35.0]
    
    if not anomalias.empty:
        print(f"⚠️ ATENÇÃO! A Inteligência Artificial detectou {len(anomalias)} sessão(ões) suspeita(s).")
        print("Motivos possíveis: Fraude de energia, falha no relógio HCA G2 ou ocupação indevida de vaga.")
    else:
        print("✅ A Inteligência Artificial não detectou anomalias. Padrão de consumo normal.")
        
    return anomalias