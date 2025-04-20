import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar e preparar os dados
def load_data(path):
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        st.error("⚠️ O arquivo está vazio ou não contém dados válidos.")
        return None
    except Exception as e:
        st.error(f"❌ Erro ao carregar os dados: {e}")
        return None
    return df

# Caminho do arquivo CSV
csv_file_path = 'C:/Users/sabri/Downloads/Aulas/data/student_depression_dataset.csv'

# Carregar os dados
df = load_data(csv_file_path)

if df is not None:
    # Título principal
    st.title("🧠📊 Análise de Dados de Depressão Estudantil")

    # Visualização inicial
    st.subheader("🔍 Visualização dos Dados")
    st.write("📝 Primeiras linhas do dataset:")
    st.write(df.head())

    # Estatísticas descritivas
    st.subheader("📈 Estatísticas Descritivas")
    st.write(df.describe())

    # Gráfico de dispersão
    st.subheader("🔄 Gráfico de Dispersão entre Colunas Numéricas")

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_columns) > 1:
        col1 = st.selectbox("🧮 Escolha a primeira coluna:", numeric_columns, key='col1')
        col2 = st.selectbox("🧮 Escolha a segunda coluna:", numeric_columns, key='col2')

        if col1 != col2:
            st.write(f"📌 Gráfico de dispersão entre **{col1}** e **{col2}**:")
            fig, ax = plt.subplots()
            ax.scatter(df[col1], df[col2], color='blue')
            ax.set_xlabel(col1)
            ax.set_ylabel(col2)
            st.pyplot(fig)
        else:
            st.warning("⚠️ Escolha colunas diferentes para o gráfico de dispersão.")
    else:
        st.warning("⚠️ Não há colunas numéricas suficientes para gerar gráficos de dispersão.")

    # Matriz de correlação
    st.subheader("🔗 Matriz de Correlação")
    correlation_matrix = df.select_dtypes(include=['float64', 'int64']).corr()

    if not correlation_matrix.empty:
        fig, ax = plt.subplots()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("⚠️ Não há colunas numéricas suficientes para calcular a correlação.")
