import pandas as pd
from funcoes import analise_descritiva, visualizar_dados

#importando dados
dados = pd.read_csv("tabela_vendas_ficticia.csv")
print(dados)


analise_descritiva(dados)
visualizar_dados(dados)


# Relatório Final
print("\nRelatório Final:")

# Insights
print("\nPrincipais Insights:")
print("- Não há tendencia de aumento de vendas com o passar do tempo.")
print("- Não há diferencia estatistica de uma categoria em relação as outras")
print("- Média de vendas diárias/mensais/anuais estável.")

# Recomendações
print("\nRecomendações:")
print("- Percebe-se que as vendas estagnaram, para aumentar as vendas tem que escalar o negócio")
print("- Investir em promoções sazonais para impulsionar vendas durante feriados.")
print("- Aumentar a quantidade de estoque para poder escalonar e vender mais.")
print("- Explorar estratégias de marketing para aumentar vendas nas demais categorias.")


# Cálculos de métricas básicas
vendas_totais = dados['Preco'].sum()
media_diaria = dados.resample('D')['Preco'].mean()
media_mensal = dados.resample('ME')['Preco'].mean()
media_anual = dados.resample('YE')['Preco'].mean()
# Métricas Básicas
print("\nMétricas Básicas:")
print(f"- Vendas Totais: R${vendas_totais:.2f}")
print("- Média Diária:")
print(media_diaria)
print("- Média Mensal:")
print(media_mensal)
print("- Média Anual:")
print(media_anual)
