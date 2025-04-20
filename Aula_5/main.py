import sys
from pathlib import Path
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Adicionar o diretório raiz ao PATH
project_root = Path().parent.resolve()
sys.path.append(str(project_root))

from adapters.repositories.kaggle_repo import KaggleRepository
from application.use_cases.auth_kaggle import AuthenticateKaggleUseCase
from application.use_cases.eda_report import GenerateEDAReportUseCase
from infrastructure.logging.logging_config import setup_logging

def main():
    st.set_page_config(page_title="Análise de Depressão Estudantil", page_icon="📊", layout="wide")
    st.title("📚 Análise Exploratória - Dataset de Depressão Estudantil")

    setup_logging()

    # Dataset info
    dataset_name = "adilshamim8/student-depression-dataset"
    file_name = "student_depression_dataset.csv"

    # Repositório Kaggle
    kaggle_repo = KaggleRepository()

    # Autenticar
    auth_use_case = AuthenticateKaggleUseCase(kaggle_repo)
    auth_use_case.execute()

    # Gerar EDA (opcional)
    eda_use_case = GenerateEDAReportUseCase(kaggle_repo)
    eda_use_case.execute(dataset_name, file_name)

    # Carregar o dataset baixado
    csv_path = Path("data") / file_name
    df = pd.read_csv(csv_path)

    st.subheader("🧠 Primeiras linhas do Dataset")
    st.dataframe(df.head())

    st.subheader("📈 Estatísticas descritivas")
    st.write(df.describe(include="all"))

    # Visualização
    st.subheader("📊 Comparação entre variáveis numéricas")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_columns) > 1:
        col1 = st.selectbox("Escolha a 1ª coluna:", numeric_columns)
        col2 = st.selectbox("Escolha a 2ª coluna:", numeric_columns)

        fig, ax = plt.subplots()
        ax.scatter(df[col1], df[col2], alpha=0.6, color='purple')
        ax.set_xlabel(col1)
        ax.set_ylabel(col2)
        st.pyplot(fig)

    st.subheader("🧮 Mapa de Correlação")
    # Apenas colunas numéricas
    corr = df.select_dtypes(include=['float64', 'int64']).corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="viridis", ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
