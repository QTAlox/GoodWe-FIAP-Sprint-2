#-------- Potência média ----------
# Para verificacao de possiveis erros de medição ou falhas no carregador

def adicionar_potencia_media(df_sessoes):
    """
    Adiciona a coluna 'potencia_media_kw' (kWh consumidos / duração em horas).
    """
    df = df_sessoes.copy()
    # Média de potência em kW durante a sessão
    df['potencia_media_kw'] = df['kwh_consumed'] / df['duration_hours']
    return df


def analisar_anomalias_potencia(df_sessoes, potencia_min=5.0, potencia_max=8.0):
    """
    Marca como suspeita toda sessão cuja potência média fique fora da faixa
    física esperada do carregador.
    - Abaixo do mínimo: possível falha (carregou devagar demais).
    - Acima do máximo: possível fraude ou erro de medição (impossível para o carregador).
    """
    print(f"⚡ Potência média das cargas - faixa esperada: {potencia_min}–{potencia_max} kW")
    df_analise = adicionar_potencia_media(df_sessoes)

    abaixo = df_analise['potencia_media_kw'] < potencia_min
    acima = df_analise['potencia_media_kw'] > potencia_max

    df_analise['motivo'] = None
    df_analise.loc[abaixo, 'motivo'] = 'potência baixa (possível falha)'
    df_analise.loc[acima, 'motivo'] = 'potência alta (possível fraude/erro)'

    anomalias_potencia_media = df_analise[abaixo | acima]

    if not anomalias_potencia_media.empty:
        print(f"⚠️ ATENÇÃO! {len(anomalias_potencia_media)} sessão(ões) com potência fora do esperado, verifique.")
    else:
        print("✅ Todas as sessões dentro da potência esperada.")

    return anomalias_potencia_media