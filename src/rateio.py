import pandas as pd

def calcular_rateio(df_sessoes, tarifa_kwh=0.95, taxa_fixa_infra=15.00):
    """
    Recebe o histórico de sessões de recarga e calcula quanto cada morador deve pagar.
    
    POR QUE ASSIM? Num condomínio, o relógio de energia do carregador é único (área comum).
    O rateio justo pega o total consumido por cada TAG/App (user_id) e multiplica 
    pela tarifa da concessionária de energia, adicionando taxas de manutenção.
    
    Parâmetros:
    - df_sessoes: DataFrame com os dados brutos de recarga.
    - tarifa_kwh: Preço médio do kWh (ex: R$ 0,95 cobrado pela Enel/Light).
    - taxa_fixa_infra: Um valor fixo cobrado apenas de quem usou no mês, para ajudar
                       na manutenção do equipamento GoodWe.
    """
    
    # Validação de segurança: se não houver dados, retorna vazio
    if df_sessoes.empty:
        print("Nenhuma sessão encontrada para rateio.")
        return pd.DataFrame()

    # 1. Agrupar os dados por usuário (soma o total de kWh e de horas que cada um usou)
    # TODO: No futuro, agrupar por MÊS também, para gerar a fatura mensal.
    resumo_usuarios = df_sessoes.groupby('user_id').agg(
        total_sessoes=('session_id', 'count'),
        total_horas=('duration_hours', 'sum'),
        total_kwh=('kwh_consumed', 'sum')
    ).reset_index()

    # 2. Aplicar as regras de negócio de tarifação
    # Custo da energia = total de kWh consumido * tarifa da concessionária
    resumo_usuarios['custo_energia_R$'] = round(resumo_usuarios['total_kwh'] * tarifa_kwh, 2)
    
    # Custo total = custo da energia + taxa de infraestrutura
    resumo_usuarios['valor_final_fatura_R$'] = round(resumo_usuarios['custo_energia_R$'] + taxa_fixa_infra, 2)
    
    # TODO: Implementar "Tarifa Dinâmica" (Bandeira Branca/Horário de Ponta). 
    # Exemplo: Se a recarga foi feita entre 18h e 21h (pico), a tarifa_kwh poderia ser R$ 1.50.
    # Isso pode ser um super diferencial no seu pitch!
    
    return resumo_usuarios

def gerar_relatorio_fechamento(df_rateio):
    """
    Gera um relatório bonitinho no terminal ou para exportar para o síndico.
    """
    print("\n" + "="*50)
    print("🔋 FECHAMENTO DE RATEIO - EV CHARGEOPS 🔋")
    print("="*50)
    
    for index, row in df_rateio.iterrows():
        print(f"Morador: {row['user_id']}")
        print(f"  - Sessões no período: {row['total_sessoes']}")
        print(f"  - Consumo total: {row['total_kwh']} kWh")
        print(f"  - Valor devido: R$ {row['valor_final_fatura_R$']}")
        print("-" * 50)
        
    total_arrecadado = df_rateio['valor_final_fatura_R$'].sum()
    print(f"💰 TOTAL ARRECADADO PARA O CONDOMÍNIO: R$ {total_arrecadado:.2f}")
    print("="*50 + "\n")