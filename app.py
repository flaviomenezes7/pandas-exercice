import pandas as pd

### 1. Carregue os conjuntos de dados "gasolina_2000+.csv" e "gasolina_2010+.csv" em dois DataFrames diferentes e combine-os em um único DataFrame.

df_data = pd.read_csv('gasolina_2000+.csv', index_col=0)
df_data2 = pd.read_csv('gasolina_2010+.csv', index_col=0)
df_combined = pd.concat([df_data, df_data2])

### 2.Investigue as colunas e entenda o conjunto de dados usando o head() e info()

df_combined.head()
df_combined.info()

### 3. Selecione a terceira entrada da coluna DATA INICIAL e verifique seu tipo.

print(type(df_combined)) # para verificar se é um DATA_FRAME

type_column = df_combined.iloc[:,2] # verificando o type da 3 column

print(type_column.dtype) 

df_combined.dtypes


### 4. Você deve ter percebido que as colunas DATA INICIAL e DATA FINAL estão formatadas como string. Utilizando o método pd.to_datetime(), converta ambas colunas para Timestamp / Datetime.

df_combined["DATA INICIAL"] = pd.to_datetime(df_combined["DATA INICIAL"])
df_combined["DATA FINAL"] = pd.to_datetime(df_combined["DATA FINAL"])


print(df_combined[["DATA INICIAL", "DATA FINAL"]].head())
type(df_combined["DATA INICIAL"].iloc[2])


### 5. Crie uma nova coluna para representar o ano e o mês(aaaa-mm), utilizando a coluna DATA FINAL como referência. 

df_combined["ANO-MES"] = df_combined["DATA FINAL"].apply(lambda x: "{}".format(x.year)) + df_combined["DATA FINAL"].apply(lambda x: "-{:02d}".format(x.month))


### 6. Utilizando o value_counts(), liste todos os tipos de produtos contidos na base de dados.

df_combined["PRODUTO"].value_counts()

### 7. Filtre o DataFrame para obter apenas dados da 'GASOLINA COMUM'. Grave em uma nova variável.

commum_gas = df_combined[df_combined["PRODUTO"] == 'GASOLINA COMUM']
commum_gas.head(5)

### 8. Qual o preço médio de revenda da gasolina em agosto de 2008?

df_combined[df_combined["ANO-MES"] == '2008-08']["PREÇO MÉDIO REVENDA"].mean()

### 9. Qual o preço médio de revenda da gasolina em maio de 2014 em São Paulo?

df_combined[(df_combined["ANO-MES"] == '2008-05') & (df_combined["ESTADO"] == 'SAO PAULO')]["PREÇO MÉDIO REVENDA"].mean()

### 10. Você conseguiria descobrir em qual(quais) estado(s) a gasolina ultrapassou a barreira dos R$ 5,00? E quando isso ocorreu?

df_combined[df_combined["PREÇO MÉDIO REVENDA"] > 5][["ESTADO", "ANO-MES", "PREÇO MÉDIO REVENDA"]].head(10)

### 11. Qual a média de preço dos estados da região sul em 2012?

df_aux = df_combined[(df_combined["DATA FINAL"].apply(lambda x: x.year) == 2012)]  # filtro auxiliar especifico para o ano de 2012
df_aux[df_aux["REGIÃO"] == "SUL"]["PREÇO MÉDIO REVENDA"].mean()

