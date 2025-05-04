import pandas as pd
import plotly.express as px
import streamlit as st

# lendo os dados
car_data = pd.read_csv('./data/vehicles.csv')

# criar um botão para o histograma
hist_button = st.button('Criar histograma')

# se o botão for clicado
if hist_button:
    # escrever uma mensagem
    st.write('Criando um Histograma para a coluna odometer')

    # criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # exibir o histograma Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

# criar uma caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar um gráfico de dispersão')

# se a caixa de seleção for selecionada
if build_scatter:
    st.write('Criando um Gráfico de dispersão entre odometer e price')

    # criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # exibir o gráfico de dispersão Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)