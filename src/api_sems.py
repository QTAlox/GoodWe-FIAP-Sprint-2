import pandas as pd
import random
from datetime import datetime, timedelta

def formatar_duracao(horas):
    """Converte horas decimais (ex: 2.5) em texto legível 'HH:MM' (ex: '02:30')."""
    total_min = round(horas * 60)
    h, m = divmod(total_min, 60)
    return f'{h:02d}:{m:02d}'

def obter_dados_sessoes_mock(num_sessoes=20):
    """
    Simula o consumo de dados da API SEMS da GoodWe.
    POR QUE ISSO É NECESSÁRIO? Para prototipar, precisamos de dados. 
    Na Sprint 02, mockar (simular) a API é uma prática recomendada quando 
    não há acesso ao hardware real.
    """
    dados = []
    usuarios = ['User_01_Ap101', 'User_02_Ap102', 'User_03_Ap201', 'User_04_Ap202']
    
    agora = datetime.now()
    
    for i in range(num_sessoes):
        # Sorteia um usuário aleatório
        usuario = random.choice(usuarios)
        
        # Simula uma recarga nos últimos 7 dias
        dias_atras = random.randint(0, 7)
        duracao_horas = random.uniform(1.5, 6.0) # Duração entre 1.5h e 6h
        horas_atras = random.uniform(duracao_horas, duracao_horas + 10)  # sempre >= duração
        hora_inicio = agora - timedelta(days=dias_atras, hours=horas_atras)
        hora_fim = hora_inicio + timedelta(hours=duracao_horas)
        
        # Simula o consumo em kWh (Carregadores AC costumam entregar ~7 a 22 kW por hora)
        # Vamos simular uma média de 7kW/h
        consumo_kwh = round(duracao_horas * random.uniform(6.5, 7.5), 2)
        
        dados.append({
            'session_id': f'SEMS_{i:04d}',
            'user_id': usuario,
            'start_time': hora_inicio,
            'end_time': hora_fim,
            'duration_hours': round(duracao_horas, 2),
            'kwh_consumed': consumo_kwh
        })

    df_sessoes = pd.DataFrame(dados)
    df_sessoes['start_time'] = df_sessoes['start_time'].dt.floor('s')
    df_sessoes['end_time'] = df_sessoes['end_time'].dt.floor('s')


    # formata duration_hours em duracao_recarga (HH:MM) para exibição no log e relatórios
    df_sessoes['duracao_recarga'] = df_sessoes['duration_hours'].apply(formatar_duracao)

    return df_sessoes
