import mysql.connector

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

def create_table():
    mycursor.execute("CREATE TABLE alunos (Id INT AUTO_INCREMENT PRIMARY KEY, Nome VARCHAR(255), Matrícula VARCHAR(255), Turma VARCHAR(255))")
    print("Tabela criada com sucesso!")

#create_table()

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

def view_data():
    sql = "SELECT * FROM alunos"

    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

#view_data()


def view_filter():
    sql = "SELECT * FROM alunos WHERE Turma = 'BCW23' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

#view_filter()

def view_filter_like():
    sql = "SELECT * FROM alunos WHERE Nome LIKE '%Lima%' "
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

#view_filter_like()

def update_where():
    sql = "UPDATE alunos SET Turma = 'BCW25' WHERE Nome ='Carlos Augusto' "

    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,'Linha(s) alterada(s)!')

#update_where()

def del_where():
    sql = "DELETE FROM alunos WHERE Nome = 'José Vinicius'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,'Linha(s) alterada(s)!')

#del_where()

def drop_table():
    sql = "DROP TABLE alunos"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,'Linha(s) alterada(s)!')

#drop_table()

def drop_database():
    mycursor.execute("DROP DATABASE sistema_escolar_soul_on")
    print("Database deletado com sucesso!")

drop_database()