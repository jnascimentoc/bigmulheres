#Atividade Prática: Através do Kaggle, procurem outros datasets e apliquem os comandos trabalhados na aula anterior.

##Doctaralia##
import pandas as pd
df_simpsons = pd.read_csv('simpsons_characters.csv')
print("--------------------------------")
print(df_simpsons.head())
print("--------------------------------")
print(df_simpsons.tail())
print("--------------------------------")
print(df_simpsons.to_string()) 
print("--------------------------------")
df_personagem = df_simpsons[df_simpsons['name'] == 'Maggie Simpson']
print(df_personagem)
print("--------------------------------")
pd.set_option('display.max_rows',10)

##Doctoralia##
import pandas as pd
df_doctoralia = pd.read_csv('doctoralia_br.csv')
print("--------------------------------")
print(df_doctoralia.head())
print("--------------------------------")
print(df_doctoralia.tail())
print("--------------------------------")
print(df_doctoralia.to_string()) 
print("--------------------------------")
df_doutor = df_doctoralia[df_doctoralia['name'] == 'Octavio Grecco']
print(df_doutor)
print("--------------------------------")
pd.set_option('display.max_rows',10)

##Movies##

import pandas as pd
df_movies = pd.read_csv('disney_plus_titles.csv')
print("--------------------------------")
print(df_movies.head())
print("--------------------------------")
print(df_movies.tail())
print("--------------------------------")
print(df_movies.to_string()) 
print("--------------------------------")
df_titulo = df_movies[df_movies['title'] == 'Annie']
print(df_titulo)
print("--------------------------------")
pd.set_option('display.max_rows',10)

##Clothes##

import pandas as pd
df_clothes = pd.read_csv('clothes_price.csv')
print(df_clothes.head())
print("--------------------------------")
print(df_clothes.tail())
print("--------------------------------")
print(df_clothes.to_string()) 
print("--------------------------------")
df_marca = df_clothes[df_clothes['Brand'] == 'Puma']
print(df_marca)
print("--------------------------------")
pd.set_option('display.max_rows',10)