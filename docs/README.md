# EV ChargeOps - GoodWe & FIAP Enterprise Challenge

**Plataforma em Python para gestão de recargas compartilhadas de veículos elétricos, com controle de sessões, rateio justo por kWh, integração com GoodWe SEMS e IA para perfis de uso e detecção de anomalias.**

## 📌 Sobre o Projeto
Este projeto foi desenvolvido para a **Sprint 02 do Enterprise Challenge 2026**. O objetivo é resolver o problema operacional de infraestruturas de recarga compartilhadas (condomínios e campi universitários), transformando dados brutos do carregador GoodWe HCA G2 em inteligência acionável e faturamento individual justo.

## 🚀 O que foi implementado (Sprint 02)
Com base na arquitetura definida na Sprint 01, implementamos um protótipo funcional contendo os seguintes módulos centrais:

1. **Módulo de Rateio com Tarifa Dinâmica (`rateio.py`):** Lógica central que agrupa o consumo por usuário e aplica regras de negócio avançadas. O sistema cobra um valor mais alto em horários de pico (18h-21h) e aplica descontos de madrugada, garantindo justiça financeira e otimização da rede.
2. **Integração GoodWe SEMS (`api_sems.py`):** Simulador de ingestão de dados (Mock) gerando telemetrias aleatórias de recarga em formato Pandas DataFrame, vital para validar a lógica em um ambiente de prototipação sem hardware físico.
3. **Módulo de Inteligência Artificial (`ai_module.py`):** Papel estrutural no sistema atuando como auditor. Utiliza o algoritmo **Isolation Forest (Scikit-Learn)** para varrer os dados antes do fechamento financeiro, detectando anomalias como consumo irreal (fraudes) ou picos de energia (falhas no equipamento).
4. **Persistência de Dados (`database.py`):** Integração com banco de dados relacional **SQLite** para armazenar o histórico de recargas e as faturas geradas de forma nativa e leve.
5. **Painel do Síndico (`dashboard.py`):** Interface visual em **Streamlit** gerando gráficos e tabelas para acompanhamento prático.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.11+
* **Manipulação de Dados:** Pandas
* **Inteligência Artificial:** Scikit-Learn (Isolation Forest)
* **Banco de Dados:** SQLite (Nativo do Python)
* **Interface Gráfica:** Streamlit

## ⚙️ Instruções de Execução

**1. Preparação do Ambiente Virtual**
Abra o terminal na pasta raiz do projeto e crie/ative o ambiente virtual:
```bash
python -m venv .venv
# Para ativar no Windows:
.\.venv\Scripts\activate
# Para ativar no Mac/Linux:
source .venv/bin/activate