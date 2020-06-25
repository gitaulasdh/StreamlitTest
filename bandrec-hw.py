import streamlit as st
import pandas as pd


# Text/Title
st.title("Recomendação de Bandas")

# Radio Buttons
pais = st.radio("Escolha o país",("Estados Unidos","Reino Unido", "Brasil"))



# Capturar input do usuário e fazer a consulta
nome = st.text_input("Digite o nome da Banda / Artista","Digite aqui..")
