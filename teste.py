import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf

st.title('FIAP LUB')

with st.container():
  st.subheader("Deploy do Método de :blue[Rede Neurais Recorrentes]")
  st.write("Abaixo é possivel realizar a previsão do preço do petróleo wit selecionando a data desejada e clicando no botão Fazer Previsão")
