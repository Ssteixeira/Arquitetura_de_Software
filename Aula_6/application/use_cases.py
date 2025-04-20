# Arquivo: application/use_cases.py
import pandas as pd
from pandas_profiling import ProfileReport

class SimpleEDAAdapter:
    def generate_report(self, df):
        """Gera um relatório EDA simples para o DataFrame fornecido."""
        # Cria o relatório de EDA utilizando o pandas_profiling
        profile = ProfileReport(df, title="Simple EDA Report", explorative=True)
        profile.to_file("eda_report.html")  # Salva o relatório em um arquivo HTML

class MLUseCases:
    def __init__(self):
        self.profiler_adapter = SimpleEDAAdapter()
    
    def profile_data(self, csv_filename):
        """Carrega os dados e gera um relatório EDA"""
        # Carregar o arquivo CSV
        df = pd.read_csv(csv_filename)
        # Gerar o relatório EDA
        self.profiler_adapter.generate_report(df)
