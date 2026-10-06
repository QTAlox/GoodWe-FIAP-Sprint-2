import pandas as pd

def calcular_custo_sessao(row, tarifa_base=0.95):
    """Aplica a tarifa dinâmica baseada na hora de início."""
    hora = row['start_time'].hour
    if 18 <= hora <= 21:
        return row['kwh_consumed'] * (tarifa_base * 1.5) # +50% no pico
    elif 0 <= hora <= 5:
        return row['kwh_consumed'] * (tarifa_base * 0.8) # -20% na madrugada
    return row['kwh_consumed'] * tarifa_base

def calcular_rateio(df_sessoes, tarifa_base=0.95, taxa_fixa_infra=15.00):
    if df_sessoes.empty:
        return pd.DataFrame()
        
    # Calcula o custo exato de cada sessão individualmente usando a IA da tarifa dinâmica
    df_sessoes['custo_sessao_R$'] = df_sessoes.apply(lambda row: calcular_custo_sessao(row, tarifa_base), axis=1)

    # Agrupa os dados por utilizador, somando agora também o custo em Reais
    resumo_usuarios = df_sessoes.groupby('user_id').agg(
        total_sessoes=('session_id', 'count'),
        total_kwh=('kwh_consumed', 'sum'),
        **{'custo_energia_R$': ('custo_sessao_R$', 'sum')}
    ).reset_index()

    # Aplica arredondamentos e a taxa fixa
    resumo_usuarios['total_kwh'] = round(resumo_usuarios['total_kwh'], 2)
    resumo_usuarios['custo_energia_R$'] = round(resumo_usuarios['custo_energia_R$'], 2)
    resumo_usuarios['valor_final_fatura_R$'] = round(resumo_usuarios['custo_energia_R$'] + taxa_fixa_infra, 2)
    
    return resumo_usuarios


def gerar_relatorio_fechamento(df_rateio):
    if df_rateio.empty:
        print('Nao ha dados processados para gerar o relatorio.')
        return

    print('\n' + '=' * 50)
    print('FECHAMENTO DE RATEIO - EV CHARGEOPS')
    print('=' * 50)
    for _, row in df_rateio.iterrows():
        print(f"Usuario: {row['user_id']}")
        print(f"  Sessoes: {row['total_sessoes']}")
        print(f"  Consumo: {row['total_kwh']:.2f} kWh")
        print(f"  Custo de energia: R$ {row['custo_energia_R$']:.2f}")
        print(f"  Total devido: R$ {row['valor_final_fatura_R$']:.2f}")
        print('-' * 50)