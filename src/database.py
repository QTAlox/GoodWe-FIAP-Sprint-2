# src/database.py
import sqlite3
import pandas as pd

def guardar_no_banco(df_sessoes, df_rateio, nome_banco="ev_chargeops.db"):
    """
    Guarda os dados processados numa base de dados SQLite.
    
    POR QUE FAZER ISTO? 
    Para um protótipo, o SQLite é a melhor escolha de SQL. Não requer instalação 
    de servidores, cria um ficheiro local (.db) e permite consultas SQL reais 
    para o caso do vosso grupo querer ligar um dashboard (ex: PowerBI ou Streamlit) depois.
    """
    
    if df_sessoes.empty or df_rateio.empty:
        print("⚠️ Sem dados processados para guardar na base de dados.")
        return

    print(f"\n💾 A guardar dados na base de dados local ({nome_banco})...")
    
    # Cria a ligação ao ficheiro da base de dados (se o ficheiro não existir, o Python cria-o na hora)
    conn = sqlite3.connect(nome_banco)
    
    try:
        # O Pandas é incrível: a função 'to_sql' cria a tabela SQL automaticamente,
        # define os tipos das colunas e insere todas as linhas de uma só vez!
        
        # Guardamos as sessões brutas
        df_sessoes.to_sql('historico_sessoes', conn, if_exists='replace', index=False)
        
        # Guardamos o teu cálculo de rateio
        df_rateio.to_sql('faturas_rateio', conn, if_exists='replace', index=False)
        
        print("✅ Dados guardados com sucesso com SQL nas tabelas 'historico_sessoes' e 'faturas_rateio'!")
        
    except Exception as e:
        print(f"❌ Erro ao guardar na base de dados: {e}")
        
    finally:
        # É uma boa prática de engenharia fechar sempre a ligação à base de dados no fim
        conn.close()