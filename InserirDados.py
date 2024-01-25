import csv
import os
import csv
from faker import Faker
import random

#Inserir e Coletar dados
def criar_arquivo_csv():
    # Cria um arquivo CSV se não existir
    if not os.path.exists('dados_vendas.csv'):
        with open('dados_vendas.csv', 'w', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            # Escreve o cabeçalho
            escritor_csv.writerow(['Nome', 'Valor', 'Data', 'Categoria'])

def inserir_dados_venda(nome, valor,data_venda, categoria):
    
    # Abre o arquivo CSV para adicionar uma nova linha
    with open('dados_vendas.csv', 'a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        # Escreve os dados da venda
        escritor_csv.writerow([nome, valor, data_venda, categoria])

def coletar_dados_vendas():
    # Abre o arquivo CSV para leitura
    with open('dados_vendas.csv', 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        # Ignora o cabeçalho
        next(leitor_csv)
        
        # Coleta e exibe os dados de venda
        for linha in leitor_csv:
            print(f"Nome: {linha[0]}, Valor: {linha[1]}, Data: {linha[2]}, Categoria: {linha[3]}")

# criando arquivo de vendas
criar_arquivo_csv()

# Inserir dados de venda
inserir_dados_venda('Produto A', 50.00,'20/04/1998', 'Eletrônicos')
inserir_dados_venda('Produto B', 30.00,'14/05/2004', 'Roupas')

# Coletar e exibir dados de venda
coletar_dados_vendas()

#Criando dados falsos para tratar eles
# Inicializa o Faker
fake = Faker()

# Lista de 10 categorias
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Calçados', 'Esportes', 'Beleza', 'Livros', 'Móveis', 'Jogos', 'Acessórios']

# Gera dados fictícios e escreve no arquivo CSV
with open('tabela_vendas_ficticia.csv', 'w', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)
    
    # Escreve o cabeçalho
    escritor_csv.writerow(['Produto', 'Preco', 'Data', 'Categoria'])

    # Gera 100 linhas de dados fictícios
    for _ in range(1000):
        produto = fake.word()
        preco = round(random.uniform(10.0, 200.0), 2)
        data_venda = fake.date_time_this_decade()
        categoria = random.choice(categorias)  # Escolhe aleatoriamente uma categoria

        # Escreve a linha no arquivo CSV
        escritor_csv.writerow([produto, preco, data_venda, categoria])

print("Tabela fictícia de vendas com categorias gerada com sucesso.")

















