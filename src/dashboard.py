# src/dashboard.py
import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="EV ChargeOps", layout="wide")
st.title("⚡ EV ChargeOps - Painel do Síndico")

# Ligar à base de dados gerado pelo main.py
conn = sqlite3.connect("ev_chargeops.db")

# Ler os dados
try:
    df_faturas = pd.read_sql_query("SELECT * FROM faturas_rateio", conn)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Faturação do Mês por Morador")
        st.dataframe(df_faturas, use_container_width=True)
        
    with col2:
        st.subheader("Consumo Total de Energia (kWh)")
        st.bar_chart(df_faturas, x="user_id", y="total_kwh")
        
except Exception as e:
    st.error("Por favor, executa primeiro o ficheiro 'python src/main.py' para gerar a base de dados.")

conn.close()