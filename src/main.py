from api_sems import obter_dados_sessoes_mock
from rateio import calcular_rateio, gerar_relatorio_fechamento
from ai_module import analisar_anomalias

def main():
    print("Iniciando plataforma EV ChargeOps...\n")
    
    # Passo 1: Ingestão de Dados (Simulando API GoodWe SEMS)
    print("📡 Conectando ao GoodWe SEMS e baixando histórico de recargas...")
    df_sessoes = obter_dados_sessoes_mock(num_sessoes=30)
    print(f"✅ Sucesso! {len(df_sessoes)} sessões recuperadas.\n")
    
    # Passo 2: Inteligência Artificial (Auditoria dos dados)
    # Fazemos isso ANTES do rateio, pois se houver erro de medição, o rateio pode ser pausado.
    anomalias = analisar_anomalias(df_sessoes)
    
    # Passo 3: Rateio e Faturamento
    print("\n💸 Calculando rateio individual dos usuários...")
    # Chamamos as funções criadas por você no rateio.py
    df_faturamento = calcular_rateio(df_sessoes, tarifa_kwh=0.95, taxa_fixa_infra=15.00)
    
    # Passo 4: Exibir Resultados
    gerar_relatorio_fechamento(df_faturamento)
    
    # TODO FINAL: O ideal para o Pitch é criar uma interface. 
    # Vocês podem usar a biblioteca Streamlit depois para transformar esses "prints" 
    # numa tela web muito bonita e visual.

if __name__ == "__main__":
    main()