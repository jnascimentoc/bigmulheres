#Integração PANDAS + MySQL
#No terminal: pip install sqlalchemy pymysql

#Codigo arquivo .py
from sqlalchemy import create_engine
import pandas as pd 
host = 'localhost'
user = 'root'
password = 'senac%40123'
database = 'mulherestech'

#(ferramenta+ferramenta de integracao://)
engine=create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
df = pd.read_sql('alunos', con = engine) #Para entender que tem uma engine do sql para o acesso.
print(df)

