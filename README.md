Sabrinna de Souza Teixeira Santos

Curso de Engenharia de Software 

Disciplina de Arquitetura de Software – 2025

🧠 Projeto de Análise Preditiva de Depressão em Estudantes
---------------------------
📚 Disciplina: Arquitetura de Software
📌 Objetivo do Projeto
Este repositório tem como finalidade apresentar, de forma estruturada, as atividades desenvolvidas na disciplina de Arquitetura de Software, aplicando conceitos como modularidade, organização de projetos, boas práticas de desenvolvimento e integração com análise de dados.
Utilizando um dataset real sobre saúde mental de estudantes universitários, o projeto contempla desde o pré-processamento dos dados até a construção e avaliação de modelos de Machine Learning, com foco na predição da depressão.

📁 Dataset Utilizado
---------
Nome: Student Mental Health

Fonte: Kaggle - Sadman Arafat

Registros: 1010

Variáveis: 17 colunas com dados demográficos, acadêmicos e comportamentais

Exemplos de variáveis:  Age, Gender, Year, CGPA (coeficiente acadêmico)

Indicadores binários sobre: estresse, bullying, pressão familiar, problemas financeiros, etc.
Depression: variável alvo (Sim ou Não)
O conjunto de dados foi escolhido por sua relevância social e pela possibilidade de análise preditiva com foco em soluções para a saúde estudantil.

-----------
🧱 Arquitetura Modular
---------
A estrutura do projeto foi organizada de forma a aplicar o conceito de modularidade, separando responsabilidades em diferentes diretórios:
📦 projeto
 ┣ 📂 data              # Conjunto de dados original e tratados
 ┣ 📂 eda               # Análises exploratórias (notebooks e gráficos)
 ┣ 📂 models            # Scripts de treinamento e avaliação de modelos
 ┣ 📂 logs              # Arquivos de log das execuções
 ┣ 📜 main.py           # Script principal do pipeline

------------
🔎 Análise e Modelagem
-------
Durante o desenvolvimento, foram realizadas as seguintes etapas:

✅ Análise Exploratória (EDA)
Limpeza e tratamento dos dados
Visualizações com seaborn, matplotlib e pandas
Análise de correlação e impacto de variáveis na depressão

✅ Treinamento de Modelos
Algoritmos utilizados:
XGBoost (melhor desempenho)
LightGBM
AdaBoost
Métricas avaliadas: Acurácia, Recall, Precisão, ROC-AUC
Balanceamento de classes com técnicas como oversampling

✅ Interpretabilidade com SHAP
Geração de gráficos SHAP (beeswarm, barplot, waterfall)
Identificação das variáveis com maior impacto no diagnóstico
Houve a implementação da biblioteca Streamlit

O modelo XGBoost apresentou melhor equilíbrio entre sensibilidade e precisão, sendo o mais eficaz na predição da depressão entre os estudantes.
---------

💡 Conclusões
-------
A arquitetura proposta favoreceu o desenvolvimento ordenado do projeto.
O modelo XGBoost foi eficaz na detecção da depressão com base em múltiplos fatores sociais e acadêmicos.
A utilização do SHAP proporcionou insights valiosos, revelando que baixa performance acadêmica, pressão familiar e bullying são os principais fatores preditivos.
O projeto demonstrou, de forma prática, a aplicação de conceitos de arquitetura de software em projetos de ciência de dados.

Kaggle - Student Mental Health Dataset. Disponível em: https://www.kaggle.com/datasets/sadmanarafat/student-mental-health

