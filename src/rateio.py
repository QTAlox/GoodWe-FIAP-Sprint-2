import pandas as pd

def calcular_rateio(df_sessoes, tarifa_kwh=0.95, taxa_fixa_infra=15.00):
    """
    Recebe o histórico de sessões de recarga e calcula quanto cada morador deve pagar.
    
    POR QUE ASSIM? Num condomínio, o relógio de energia do carregador é único (área comum).
    O rateio justo pega o total consumido por cada utilizador e multiplica 
    pela tarifa da concessionária de energia, adicionando taxas de manutenção.
    
    Parâmetros:
    - df_sessoes: DataFrame com os dados brutos de recarga (vindos da API/Mock).
    - tarifa_kwh: Preço médio do kWh cobrado pela concessionária (ex: Enel/Light).
    - taxa_fixa_infra: Valor fixo para ajudar na manutenção do equipamento GoodWe.
    """
    
    # 1. Validação de Segurança (Fail-Fast)
    # POR QUE FAZER ISTO? Se a integração com a GoodWe falhar e não enviar dados,
    # o nosso código avisa educadamente em vez de "crashar" o sistema inteiro.
    if df_sessoes.empty:
        print("Aviso: Nenhuma sessão encontrada para processar o rateio.")
        return pd.DataFrame()
        
    # 2. Validação de Colunas
    # Garante que os dados que chegaram têm a estrutura exata que a nossa matemática precisa.
    colunas_obrigatorias = ['user_id', 'session_id', 'duration_hours', 'kwh_consumed']
    for col in colunas_obrigatorias:
        if col not in df_sessoes.columns:
            raise ValueError(f"Erro Crítico: A coluna '{col}' não foi recebida nos dados das sessões.")

    # 3. Agrupamento dos consumos por utilizador
    # O Pandas junta todas as linhas do mesmo 'user_id' e faz a soma (sum) dos kWh e horas,
    # além de contar (count) quantas sessões de recarga cada um fez.
    # TODO Futuro: Agrupar também por 'Mês/Ano' para permitir faturas mensais, não apenas um total global.
    resumo_usuarios = df_sessoes.groupby('user_id').agg(
        total_sessoes=('session_id', 'count'),
        total_horas=('duration_hours', 'sum'),
        total_kwh=('kwh_consumed', 'sum')
    ).reset_index()

    # 4. Limpeza de Dados (Arredondamento)
    # POR QUE FAZER ISTO? O Python às vezes cria dízimas (ex: 45.0000001) ao somar números com casas decimais.
    # Arredondamos para 2 casas para manter os valores consistentes.
    resumo_usuarios['total_horas'] = round(resumo_usuarios['total_horas'], 2)
    resumo_usuarios['total_kwh'] = round(resumo_usuarios['total_kwh'], 2)

    # 5. Aplicação das Regras de Negócio Financeiras
    # Custo da energia = total de kWh consumido * tarifa da concessionária
    # TODO Futuro: Implementar "Tarifa Dinâmica". Se a recarga foi no horário de ponta (ex: 18h-21h), cobrar mais caro.
    resumo_usuarios['custo_energia_R$'] = round(resumo_usuarios['total_kwh'] * tarifa_kwh, 2)
    
    # Custo total da fatura = custo da energia gasta + taxa fixa de infraestrutura
    resumo_usuarios['valor_final_fatura_R$'] = round(resumo_usuarios['custo_energia_R$'] + taxa_fixa_infra, 2)
    
    return resumo_usuarios


def gerar_relatorio_fechamento(df_rateio):
    """
    Lê a tabela final de rateio e imprime um relatório limpo e legível no terminal.
    Este relatório serve como "Evidência de funcionamento" para a Sprint 02.
    """
    
    # Prevenção: se a função de cálculo falhou ou não encontrou dados, não tentamos imprimir.
    if df_rateio.empty:
        print("Não há dados processados para gerar o relatório do síndico.")
        return

    print("\n" + "="*50)
    print("🔋 FECHAMENTO DE RATEIO - EV CHARGEOPS 🔋")
    print("="*50)
    
    # O iterrows() permite-nos analisar o DataFrame linha a linha
    for _, row in df_rateio.iterrows():
        print(f"Morador: {row['user_id']}")
        print(f"  - Sessões no período: {row['total_sessoes']}")
        
        # A formatação :.2f nas variáveis (ex: {variavel:.2f}) é crucial.
        # Ela força o Python a mostrar sempre os cêntimos, imprimindo 'R$ 15.00' em vez de 'R$ 15.0'
        print(f"  - Consumo total: {row['total_kwh']:.2f} kWh")
        print(f"  - Custo energia: R$ {row['custo_energia_R$']:.2f}")
        print(f"  - Taxa manutenção GoodWe: R$ 15.00")
        print(f"  - VALOR TOTAL DEVIDO: R$ {row['valor_final_fatura_R$']:.2f}")
        print("-" * 50)
        
    # Soma de todo o dinheiro que o condomínio vai arrecadar para pagar a conta de luz da área comum
    total_arrecadado = df_rateio['valor_final_fatura_R$'].sum()
    print(f"💰 TOTAL ARRECADADO PARA O CONDOMÍNIO: R$ {total_arrecadado:.2f}")
    print("="*50 + "\n")