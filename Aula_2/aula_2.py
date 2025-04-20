import os
import pandas as pd
import matplotlib.pyplot as plt
from autoviz.AutoViz_Class import AutoViz_Class
from kaggle.api.kaggle_api_extended import KaggleApi
import sweetviz as sv
import dtale
import zipfile

# CONFIGURAÇÕES
dataset_name = "adilshamim8/student-depression-dataset"
file_name = "student_depression_dataset.csv"  # Corrigido para o nome correto do arquivo
download_path = os.path.join(os.getcwd(), "data")

# GARANTIR QUE A PASTA DE DESTINO EXISTE
os.makedirs(download_path, exist_ok=True)

# AUTENTICAÇÃO KAGGLE
try:
    api = KaggleApi()
    api.authenticate()
    print("✅ Autenticação bem-sucedida!")
except Exception as e:
    print(f"❌ Erro ao autenticar na Kaggle API: {e}")
    exit()

# DOWNLOAD DO DATASET
try:
    api.dataset_download_files(dataset_name, path=download_path, unzip=False)
    print("📦 Dataset baixado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao baixar dataset: {e}")
    exit()

# EXTRAIR O ZIP
zip_path = os.path.join(download_path, f"{dataset_name.split('/')[-1]}.zip")
if os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)
    print("✅ Arquivo ZIP extraído!")
else:
    print("❌ Arquivo ZIP não encontrado.")
    exit()

# LISTAR ARQUIVOS EXTRAÍDOS (opcional para confirmar o nome correto do arquivo)
print("\n📁 Arquivos extraídos:")
for filename in os.listdir(download_path):
    print(filename)

# CARREGAR O CSV
csv_path = os.path.join(download_path, file_name)
if not os.path.exists(csv_path):
    print(f"❌ CSV '{file_name}' não encontrado na pasta {download_path}")
    exit()

df = pd.read_csv(csv_path)

# INFORMAÇÕES BÁSICAS DO DATASET
print("\n📊 Informações do DataFrame:")
print(df.info())
print("\n🧠 Primeiras 10 linhas:")
print(df.head(10))
print("\n📈 Estatísticas gerais (números):")
print(df.describe().round())
print("\n🔠 Estatísticas de colunas categóricas:")
print(df.describe(include=["object", "category"]))
print("\n❓ Valores ausentes:")
print(df.isnull().sum())

# AUTOVIZ
print("\n🚀 Gerando visualizações automáticas com AutoViz...")
av = AutoViz_Class()
report = av.AutoViz(csv_path)  # AutoViz funciona melhor com caminho de arquivo

# SWEETVIZ
print("\n🍬 Gerando relatório do Sweetviz...")
sweetviz_report = sv.analyze(df)
sweetviz_report.show_html("sweetviz_report.html")
print("✅ Relatório do Sweetviz salvo como sweetviz_report.html")

# DTALE
print("\n🌐 Abrindo D-Tale no navegador...")
d = dtale.show(df)
d.open_browser()
