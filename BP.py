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
df = pd.read_excel('BP.xlsx')
df["Data"] = pd.to_datetime(df["Data"])
df.info()
df=df.sort_values("Data")
df.dropna()

df['Month']=df['Data'].apply(lambda x: str(x.year) + '-' + str(x.month))
month = st.sidebar.selectbox("Selecione o mês", df['Month'].unique())

df_filtered = df[df["Month"] == month]

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

fig1 = px.pie(df, values='Ativo circulante', names='Month', title='Ativo circulante')
col3.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(df, values='Ativo não circulante', names='Month', title='Ativo não circulante')
col4.plotly_chart(fig2, use_container_width=True)

fig3 = px.pie(df, values='Passivo circulante', names='Month', title='Passivo circulante')
col5.plotly_chart(fig3, use_container_width=True)

st.divider()

col6, col7= st.columns(2)

fig4 = px.pie(df, values='Patrimonio liquido', names='Month', title='Patrimônio liquido')
col6.plotly_chart(fig4, use_container_width=True)

fig5 = px.pie(df, values='Total do passivo e PL', names='Month', title='Total do Passivo e Patrimônio liquido')
col7.plotly_chart(fig5, use_container_width=True)


endividamento_geral = float(passivo_circulante/ativo_circulante)*100