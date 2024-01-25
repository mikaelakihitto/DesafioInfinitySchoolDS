import pandas as pd 

#importando dados
dados = pd.read_csv("tabela_vendas_ficticia.csv")

#limpando dados e processando dados
print(dados.isnull())

#processando dados
dados["Data"] = dados["Data"].str[:10]
dados["Data"] = pd.to_datetime(dados["Data"])


#print(dados.info())
#print(dados.describe())


