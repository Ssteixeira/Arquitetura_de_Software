import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


class SimpleEDAAdapter:
    def profile(self, csv_path: str):
        df = pd.read_csv(f"data/{csv_path}")

        # Cria a pasta de relatórios, se não existir
        os.makedirs("reports", exist_ok=True)
        os.makedirs("reports/plots", exist_ok=True)

        # Gera estatísticas e salva em .txt
        report_path = f"reports/simple_eda_{csv_path.replace('.csv', '')}.txt"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("### Resumo Estatístico ###\n")
            f.write(str(df.describe(include="all")))
            f.write("\n\n### Tipos de Dados ###\n")
            f.write(str(df.dtypes))
            f.write("\n\n### Valores Nulos ###\n")
            f.write(str(df.isnull().sum()))
            f.write("\n")

        # Gera gráficos para colunas numéricas
        for col in df.select_dtypes(include="number").columns:
            plt.figure(figsize=(6, 4))
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f'Distribuição de {col}')
            plt.xlabel(col)
            plt.ylabel('Frequência')
            plt.tight_layout()
            plot_path = f"reports/plots/{col}_dist.png"
            plt.savefig(plot_path)
            plt.close()
