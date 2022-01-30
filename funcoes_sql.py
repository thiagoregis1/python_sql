import mysql.connector

#FUNÇÃO PARA CRIAR UM DATABASE LOCAL
def create_database():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE sistema_escolar_soul_on")
    print("Database criada com sucesso!")

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sistema_escolar_soul_on'
)
mycursor = mydb.cursor()

#FUNÇÃO PARA CRIAR UMA TABELA NO DATABASE LOCAL CRIADO NA FUNÇÃO ANTERIOR
def create_table():
    mycursor.execute("CREATE TABLE alunos (Id INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(255), Matrícula VARCHAR(255), Turma VARCHAR(255))")
    print("Tabela criada com sucesso!")

#create_table()

#FUNÇÃO PARA INSERIR OS DADOS NA TABELA
def insert_data():
    sql = "INSERT INTO alunos (Nome, Matrícula, Turma) VALUES (%s, %s, %s)"
    val = [
        ('José Lima', 'MAT90551', 'BCW22'),
        ('Carlos Augusto', 'MAT90552', 'BCW22'),
        ('Lívia Lima', 'MAT90553', 'BCW22'),
        ('Sandra Gomes', 'MAT90554', 'BCW23'),
        ('João Augusto', 'MAT90555', 'BCW23'),
        ('Breno Lima', 'MAT90556', 'BCW24'),
        ('José Vinícius', 'MAT90557', 'BCW25')
    ]
    mycursor.executemany(sql,val)
    mydb.commit()
    print(mycursor.rowcount, 'Linha(s) alterada(s)!')

#insert_data()

#FUNÇÃO PARA VISUALIZAR TODOS OS DADOS DA TABELA
def view_data():
    sql = "SELECT * FROM alunos"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

#view_data()

#FUNÇÃO PARA VISUALIZAR OS DADOS DA TABELA INTEIRA COM FILTRO ESPECÍFICO EM UMA DAS COLUNAS
def view_filter():
    sql = "SELECT * FROM alunos WHERE Turma = 'BCW23' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

#view_filter()


#FUNÇÃO PARA VISUALIZAR OS DADOS DA TABELA INTEIRA COM FILTRO DE 'CONTÉM'EM UMA DAS COLUNAS
def view_filter_like():
    sql = "SELECT * FROM alunos WHERE Nome LIKE '%Lima%' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

#view_filter_like()


#FUNÇÃO PARA CRIAR UMA ALTERAÇÃO EM UM CAMPO ESPECÍFICO DA TABELA
def update_where():
    sql = "UPDATE alunos SET Turma = 'BCW25' WHERE Nome ='Carlos Augusto' "

    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,'Linha(s) alterada(s)!')

#update_where()


#FUNÇÃO PARA DELETAR UMA LINHA FILTANDO POR UM CAMPO ESPECÍFICO DA TABELA
def del_where():
    sql = "DELETE FROM alunos WHERE Nome = 'José Vinicius'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,'Linha(s) alterada(s)!')

#del_where()

#FUNÇÃO PARA DELETAR A TABELA POR INTEIRA
def drop_table():
    sql = "DROP TABLE alunos"
    mycursor.execute(sql)
    mydb.commit()
    print('Tabela deletada com sucesso!')

#drop_table()

#FUNÇÃO PARA DELETAR O DATABASE INTEIRO
def drop_database():
    mycursor.execute("DROP DATABASE sistema_escolar_soul_on")
    print("Database deletado com sucesso!")

drop_database()
