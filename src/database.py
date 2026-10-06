# src/database.py
import sqlite3
import pandas as pd

def guardar_no_banco(df_sessoes, df_rateio, nome_banco="ev_chargeops.db"):
    """
    Guarda os dados processados numa base de dados SQLite.
    """
    
    if df_sessoes.empty or df_rateio.empty:
        print("⚠️ Sem dados processados para guardar na base de dados.")
        return

    print(f"\n💾 Guardando dados na base de dados local ({nome_banco})...")
    
    # Cria a ligação ao ficheiro da base de dados (se o ficheiro não existir, o Python cria-o na hora)
    conn = sqlite3.connect(nome_banco)
    
    try:
        # sessões brutas
        df_sessoes.to_sql('historico_sessoes', conn, if_exists='replace', index=False)
        
        # cálculo de rateio
        df_rateio.to_sql('faturas_rateio', conn, if_exists='replace', index=False)
        
        print("✅ Dados guardados com sucesso com SQL nas tabelas 'historico_sessoes' e 'faturas_rateio'!")
        
    except Exception as e:
        print(f"❌ Erro ao guardar na base de dados: {e}")
        
    finally:
        conn.close()