import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile

# PASSO 1: Caminho para o kaggle.json
kaggle_json_path = r"C:\Users\sabri\.kaggle\kaggle.json"

# PASSO 2: Carrega as credenciais
try:
    with open(kaggle_json_path, 'r') as file:
        dados = json.load(file)
except FileNotFoundError:
    print("❌ Arquivo kaggle.json não encontrado!")
    exit()
except json.JSONDecodeError:
    print("❌ JSON inválido!")
    exit()

# PASSO 3: Configurar variáveis de ambiente
os.environ['KAGGLE_USERNAME'] = dados['username']
os.environ['KAGGLE_KEY'] = dados['key']

# PASSO 4: Autenticar na API
try:
    api = KaggleApi()
    api.authenticate()
    print("✅ Autenticação bem-sucedida!")
except Exception as e:
    print(f"❌ Erro ao autenticar: {e}")
    exit()

# PASSO 5: Baixar dataset
dataset_name = "adilshamim8/student-depression-dataset"
download_path = r"C:\Users\sabri\Downloads\data"  # <-- pasta onde os arquivos serão salvos
os.makedirs(download_path, exist_ok=True)

try:
    api.dataset_download_files(dataset_name, path=download_path, unzip=False)
    print("📦 Download finalizado!")
except Exception as e:
    print(f"❌ Erro ao baixar o dataset: {e}")
    exit()

# PASSO 6: Extrair o zip
zip_file = os.path.join(download_path, "student-depression-dataset.zip")

if os.path.exists(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(download_path)
    print("✅ Arquivo extraído com sucesso!")
else:
    print("❌ Arquivo ZIP não encontrado.")
    exit()

# PASSO 7: Listar arquivos disponíveis
print("📁 Arquivos encontrados na pasta:")
arquivos = os.listdir(download_path)
for a in arquivos:
    print("-", a)

# PASSO 8: Tentar encontrar o .csv e carregar
csv_file = next((f for f in arquivos if f.endswith(".csv")), None)

if csv_file:
    csv_path = os.path.join(download_path, csv_file)
    df = pd.read_csv(csv_path)
    print("\n📊 Dados carregados com sucesso!")
    print(df.info())
    print(df.head())
    print(df.describe())
else:
    print("⚠️ Nenhum arquivo .csv encontrado na pasta.")
