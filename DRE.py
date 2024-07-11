import pandas as pd
import streamlit as st
import plotly.express as px
import datetime as dt
import plotly.graph_objects as go
import numpy as np
from streamlit_extras.metric_cards import style_metric_cards
st.set_option('deprecation.showPyplotGlobalUse', False)
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
df = pd.read_excel('DRE.xlsx')
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






