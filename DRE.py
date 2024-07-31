import pandas as pd
import streamlit as st
import plotly.express as px
import datetime as dt
import plotly.graph_objects as go
import numpy as np
from streamlit_extras.metric_cards import style_metric_cards

import os


st.set_page_config(layout='wide')
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #103F7A;
    }
    [data-testid="stSidebar"] * {
        color: black;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown('Desenvolvido por Emanuela Pereira')
df = pd.read_excel('Planilha.xlsx')
df["Data"] = pd.to_datetime(df["Data"])
df.info()
df=df.sort_values("Data")
df.dropna()



df['Ano']=df['Data'].apply(lambda x: str(x.year)+ '-' + str(x.year))
ano = st.sidebar.selectbox("Selecione o ano", df['Ano'].unique())

df_filtered = df[df["Ano"] == ano]

st.markdown('# Demonstração do Resultado do Exercício')
st.divider()

col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)
col6, col7 = st.columns(2)


receita_liquida = df_filtered['Receita liquida']
lucro_bruto = df_filtered['Lucro Bruto']
lucro_liquido = df_filtered['Lucro antes do IR E CSLL']


       
margem_bruta = float(lucro_bruto/receita_liquida)*100
with col1:
        st.info('Margem bruta',icon="💰")
        st.metric(label="Margem bruta",value=f"{margem_bruta:,.2f}%")
        

margem_liquida = float(lucro_liquido/receita_liquida)*100
with col2:
        st.info('Margem liquida',icon="💰")
        st.metric(label="Margem liquida",value=f"{margem_liquida:,.2f}%")

lucratividade = float(lucro_liquido/receita_liquida)*100
with col3:
        st.info('Lucratividade',icon="💰")
        st.metric(label="Lucratividade",value=f"R${lucratividade:,.2f}")


st.divider()
fig1 = px.bar(df, x='Receita liquida', y='Ano',labels={'x': 'Receita', 'y': 'Ano'},title='Receita liquida')
col4.plotly_chart(fig1,use_container_width=True)

fig2 = px.bar(df, x='Lucro Bruto', y='Ano',labels={'x': 'Lucro Bruto', 'y': 'Ano'},title='Lucro Bruto')
col5.plotly_chart(fig2,use_container_width=True)

fig3 = px.pie(df, values='Despesas operacionais', names='Ano', title='Despesas Operacionais')
col6.plotly_chart(fig3, use_container_width=True)

fig4 = px.pie(df, values='Resultado financeiro', names='Ano', title='Resultado financeiro')
col7.plotly_chart(fig4, use_container_width=True)


st.markdown('# Balanço Patrimonial')
st.divider()
ativo_circulante = df['Ativo circulante'].sum()
ativo_não_circulante = df['Ativo não circulante'].sum()
total_ativo = df['Total do ativo'].sum()
passivo_circulante = df['Passivo circulante'].sum()
patrimonio_liquido = df_filtered['Patrimonio liquido'].sum()
total_passivo_PL = df_filtered['Total do passivo e PL'].sum()

col1, col2, col3= st.columns(3)

with col1:
        st.info('Patrimonio Liquido',icon="💰")
        st.metric(label="Patrimonio Liquido",value=f"{patrimonio_liquido:,.2f}")
        
with col2:
        st.info('Total do Patrimonio Liquido e Passivo',icon="💰")
        st.metric(label="Patrimonio Liquido e Passivo",value=f"{total_passivo_PL:,.2f}")
        
endividamento_geral = float(passivo_circulante/ativo_circulante)*100

with col3:
        st.info('Endividamento Geral',icon="💰")
        st.metric(label="Endividamento Geral",value=f"{endividamento_geral:,.2f}%")
        

st.divider()
col3, col4, col5 = st.columns(3)

fig1 = px.pie(df, values='Ativo circulante', names='Ano', title='Ativo circulante')
col3.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(df, values='Ativo não circulante', names='Ano', title='Ativo não circulante')
col4.plotly_chart(fig2, use_container_width=True)

fig3 = px.pie(df, values='Passivo circulante', names='Ano', title='Passivo circulante')
col5.plotly_chart(fig3, use_container_width=True)

st.divider()

col6, col7= st.columns(2)

fig4 = px.pie(df, values='Patrimonio liquido', names='Ano', title='Patrimônio liquido')
col6.plotly_chart(fig4, use_container_width=True)

fig5 = px.pie(df, values='Total do passivo e PL', names='Ano', title='Total do Passivo e Patrimônio liquido')
col7.plotly_chart(fig5, use_container_width=True)
