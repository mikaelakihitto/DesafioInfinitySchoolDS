# Função para realizar análise descritiva
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analise_descritiva(vendas_df):
    # Informações gerais
    print("Informações Gerais:")
    print(vendas_df.info())

    # Vendas totais
    print("\nVendas Totais:")
    print(vendas_df['Preco'].sum())

    # Médias diárias, mensais, anuais
    vendas_df['Data'] = pd.to_datetime(vendas_df['Data'])
    vendas_df.set_index('Data', inplace=True)

    print("\nMédia Diária:")
    print(vendas_df.resample('D')['Preco'].mean())

    print("\nMédia Mensal:")
    print(vendas_df.resample('ME')['Preco'].mean())

    print("\nMédia Anual:")
    print(vendas_df.resample('YE')['Preco'].mean())

    # Categorias de produtos mais vendidos
    print("\nCategorias de Produtos Mais Vendidos:")
    print(vendas_df['Categoria'].value_counts())

# Função para visualizar os dados
def visualizar_dados(vendas_df):
    # Gráfico de linha para tendências temporais
    plt.figure(figsize=(10, 6))
    vendas_df.resample('ME')['Preco'].sum().plot(kind='line')
    plt.title('Tendência Temporal de Vendas')
    plt.xlabel('Data')
    plt.ylabel('Vendas')
    plt.show()

    # Gráfico de barras para categorias de produtos mais vendidos
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Categoria', data=vendas_df)
    plt.title('Categorias de Produtos Mais Vendidos')
    plt.xlabel('Categoria')
    plt.ylabel('Quantidade de Vendas')
    plt.show()


