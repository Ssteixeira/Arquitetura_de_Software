import streamlit as st
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Função para autenticação
def autenticar_kaggle():
    try:
        api = KaggleApi()
        api.authenticate()
        return api
    except Exception as e:
        st.error(f"Erro na autenticação da API Kaggle: {e}")
        return None

# Função para baixar e carregar o dataset
def baixar_e_carregar(api, dataset_name, file_name):
    pasta = "./data"
    os.makedirs(pasta, exist_ok=True)

    try:
        api.dataset_download_files(dataset_name, path=pasta, unzip=True)
        caminho_csv = os.path.join(pasta, file_name)
        if os.path.exists(caminho_csv):
            return pd.read_csv(caminho_csv)
        else:
            st.error("Arquivo CSV não encontrado após extração.")
            return None
    except Exception as e:
        st.error(f"Erro ao baixar ou carregar o dataset: {e}")
        return None

# Streamlit app
st.set_page_config(page_title="Análise de Dados - Kaggle", layout="wide")

st.title("📊 Análise Exploratória de Dados (EDA)")
st.markdown("Este app baixa um dataset do Kaggle e mostra informações básicas.")

dataset_name = st.text_input("Digite o nome do dataset Kaggle (ex: `adilshamim8/student-depression-dataset`):")
file_name = st.text_input("Nome do arquivo CSV (ex: `student_depression_dataset.csv`):")

if st.button("📥 Baixar e Analisar"):
    if dataset_name and file_name:
        with st.spinner("Autenticando e baixando..."):
            api = autenticar_kaggle()
            if api:
                df = baixar_e_carregar(api, dataset_name, file_name)
                if df is not None:
                    st.success("Dados carregados com sucesso!")

                    st.subheader("📌 Informações Gerais")
                    st.write(df.info())

                    st.subheader("📈 Estatísticas Descritivas")
                    st.dataframe(df.describe(include="all"))

                    st.subheader("❓ Valores Ausentes")
                    st.dataframe(df.isnull().sum().to_frame("Faltantes"))
    else:
        st.warning("Preencha todos os campos para continuar.")
