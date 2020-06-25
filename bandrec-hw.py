import streamlit as st
import pandas as pd
from scipy.spatial.distance import cosine
import numpy as np
from scipy.sparse import csr_matrix
import string
from fuzzywuzzy import fuzz
from sklearn.neighbors import NearestNeighbors
import warnings
warnings.filterwarnings("ignore")


# Text/Title
st.title("Recomendação de Bandas")

# Radio Buttons
pais = st.radio("Escolha o país",("Estados Unidos","Reino Unido", "Brasil"))



# Capturar input do usuário e fazer a consulta
nome = st.text_input("Digite o nome da Banda / Artista","Digite aqui..")