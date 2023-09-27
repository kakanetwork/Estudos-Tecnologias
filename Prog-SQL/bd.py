import sqlite3, os
from faker import Faker

fake = Faker('pt_BR')

dir_atual = os.path.dirname(os.path.abspath(__file__))
dir_bd = os.path.join(dir_atual, 'bd01')

# Cria o banco de dados
conexao = sqlite3.connect(dir_bd) 

# aponta para o banco de dados criado
cursor = conexao.cursor()

# criando tabela para o banco de dados 
cursor.execute('CREATE TABLE Minha_Tabela ( Nome text, Email text, Cpf text )')



# Inserindo valores para o banco de dados 
cursor.execute('INSERT INTO Minha_Tabela VALUES ( "Kalvin Klein", "Kalvimklain@gmail.com", "999.999.999-99")')


for _ in range(30):

    nome = fake.name()
    email = fake.email()
    cpf = fake.cpf()

    cursor.execute(f'INSERT INTO Minha_Tabela VALUES ( "{nome}", "{email}", "{cpf}" )')

# Para atualizar o BD (quando for criar tabelas apenas)
conexao.commit()

cursor.execute('SELECT * FROM Minha_Tabela')