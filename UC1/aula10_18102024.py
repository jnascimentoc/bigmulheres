# Pandas
import pandas as pd
print(pd.__version__)

#Criação de Dataset

data = {'Cargo': ['Analista', 'Gerente', 'Estagiário'],
        'Salário': [4500, 9000, 2000]}
df = pd.DataFrame(data)
print(df)

#Criação de uma série

cargos = pd.Series(['Analista', 'Gerente', 'Estagiário'], index=[1, 2, 3])
print(cargos)

#Atividade assistida

#Crie um dataset de 3 colunas com as seguintes informações: 'nome de um filme', 'ano de lançamento' e 'gênero'.
import pandas as pd 

data_cinema = {'Título': ['Cidade de Deus', 'Divertidamente 2', 'Uma linda mulher'], 
          'Ano de Lançamento': [2002,2024, 1990], 
          'Gênero': ['Drama','Animacao','Romance' ]}

data_cinema = pd.DataFrame(data_cinema)
print(data_cinema)

#Acesso a datasets externos
#https://www.kaggle.com/datasets/thebumpkin/700-classic-disco-tracks-with-spotify-data

import pandas as pd
df_disco = pd.read_csv('ClassicDisco.csv')
#df_disco = pd.read_xlsx('ClassicDisco.xlsx')
print(df_disco.head()) # Exibe as 5 primeiras linhas
print(df_disco.tail()) # Exibe as 5 últimas linhas

#Leitura de Arquivos e Filtragem:

print(df_disco.to_string()) #Exibe o DataFrame completo como uma string, útil para visualização.

print(df_disco.max_rows()) #Define o número máximo de linhas a ser exibido

#Exemplo de filtragem por colunas e linhas específicas:

df_filtrado = df_disco[df_disco['Year'] == 1979]
print(df_filtrado)

#Criação de Novas Colunas: adicionar colunas derivadas

df_disco['Duração_Minutos'] = df_disco['Duração_Segundos'] / 60