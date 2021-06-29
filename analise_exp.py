# %%
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

# %%
df = pd.read_excel('AdventureWorks.xlsx')
df.head(5)

# %%
df.shape
df.types()

# %%
#Qual a Receita total?
df["Valor Venda"].sum()

# %%
#Criar coluna de custo.
#Qual custo total?
df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

# %%
#Qual a custo total?
round(df["Custo"].sum(), 2)

# %%
#Criar coluna de lucro.
#Qual o lucro Total?
df["Lucro"] = df["Valor Venda"] - df["Custo"]

# %%
#Qual o lucro Total?
round(df["Lucro"].sum(), 2)

# %%
df.head(5)

#%%
#criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

# %%
#extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

#%%
#verificando o tipo da coluna
df["Tempo_envio"].dtype

#%%
#Media do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()

#%%
#Verificando valores faltantes
df.isnull().sum()

#%%
#tirar notacao cientifica dos numeros flutuantes
pd.options.display.float_format = '{:20,.2f}'.format

#%%
#lucro ano e marca
#Vamos agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()

#%%
#resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
lucro_ano
#%%
#Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#%%
#grafico total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

#%%
df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

#%%
df.groupby(df["Data Venda"].dt.year)["Lucro"].sum()

#%%
#selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

#%%
df_2009.head(5)

#%%
df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

#%%
df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");

#%%
df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal");

# %%
df["Tempo_envio"].describe()

# %%
#grafico de boxplot
plt.boxplot(df["Tempo_envio"]);

# %%
#histograma
plt.hist(df["Tempo_envio"])
# %%
#tempo minimo de envio
df["Tempo_envio"].min()
df["Tempo_envio"].max()
# %%
#identificando os outliers
df[df["Tempo_envio"] == 20]

#%%
df.to_csv("df_vendas_novo.csv", index=False)