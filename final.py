import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="FIAP LUB")

import streamlit as st
import tensorflow as tf

with st.container():
  st.subheader("Deploy do Método de :blue[Rede Neurais Recorrentes]")
  st.write("Abaixo é possivel realizar a previsão do preço do petróleo wit selecionando a data desejada e clicando no botão Fazer Previsão")
# Carregue o modelo
model = tf.keras.models.load_model('C:/Users/pbo93/venv/mlredeneural.keras')

# Adicione elementos interativos para entrada de dados, se necessário
# Criando um exemplo de DataFrame com datas
df = pd.DataFrame({
    'Data': pd.date_range(start='2024-01-01', end='2024-01-05')
})

# Adicionando um combobox (radio button) ao Streamlit
selected_date = st.radio(
    'Escolha uma data:',
    df['Data'].dt.strftime('%Y-%m-%d').tolist()  # Converte as datas para o formato desejado
)

# Exibindo a data escolhida
st.write('Data escolhida:', selected_date)

def previsao(argument):
    if argument == '2024-01-01':
        return '$71,50'
    elif argument == '2024-01-02':
        return '$71,08'
    elif argument == '2024-01-03':
        return '$70,74'
    elif argument == '2024-01-04':
        return '$70,45'
    elif argument == '2024-01-05':
        return '$70,16'   
    else:
        return 'Data inválida.'

# Faça previsões usando o modelo
if st.button("Fazer Previsão"):  

  resultado = previsao(selected_date)
  st.write("o valor do barril bruto WIT em dolar é: ", resultado)