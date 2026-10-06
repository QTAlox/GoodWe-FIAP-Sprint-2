# src/main.py
from api_sems import obter_dados_sessoes_mock
from rateio import calcular_rateio, gerar_relatorio_fechamento
from ai_module import analisar_anomalias
from database import guardar_no_banco  
from regras import adicionar_potencia_media, analisar_anomalias_potencia

def main():
    print("Iniciando plataforma EV ChargeOps...\n")
    
    # Passo 1: Ingestão de Dados (Simulando API GoodWe SEMS)
    print("📡 Ligando ao GoodWe SEMS e a descarregar o histórico de recargas...")
    df_sessoes = obter_dados_sessoes_mock(num_sessoes=30)
    print(f"✅ Sucesso! {len(df_sessoes)} sessões recuperadas.\n")
    
    # Passo 2: Inteligência Artificial (Auditoria dos dados)
    anomalias = analisar_anomalias(df_sessoes)

    # Passo 3: Analise de possíveis anomalias de recarga com base na potência média
    adicionar_potencia_media(df_sessoes)
    analisar_anomalias_potencia(df_sessoes)
    
    # Passo 4: Rateio e Faturação (A tua parte principal)
    print("\n💸 Calculando o rateio individual dos utilizadores...")
    df_faturamento = calcular_rateio(df_sessoes, tarifa_base=0.95, taxa_fixa_infra=15.00)
    
    # Passo 5: Exibir Resultados no Terminal
    gerar_relatorio_fechamento(df_faturamento)
    
    # Passo 6: Persistência de Dados (SQL)
    # Guarda o trabalho feito num ficheiro SQLite real
    guardar_no_banco(df_sessoes, df_faturamento)

    print("\n🚀 Processo concluído com sucesso. Protótipo pronto!")

if __name__ == "__main__":
    main()