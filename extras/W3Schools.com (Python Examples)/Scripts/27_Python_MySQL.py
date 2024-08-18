#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python MySQL
#-------------------------------------------------------------

r"""
Pré-requisitos ▼
MySQL Database
To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer.
You can download a MySQL database at https://www.mysql.com/downloads/.
"""
r"""
◘ Instalar o MYSQL WorkBench e Server ◘
  Baixar o instalador pelo site e instalar manualmente

◘ Instalar MySQL Driver ◘
  $ python -m pip install mysql-connector-python

Retorno ▼
    C:\Apps\.Developer\CMDer Mini\content
    λ python -m pip install mysql-connector-python
    Collecting mysql-connector-python
      Downloading mysql_connector_python-9.0.0-cp312-cp312-win_amd64.whl.metadata (2.0 kB)
    Downloading mysql_connector_python-9.0.0-cp312-cp312-win_amd64.whl (14.3 MB)
       ---------------------------------------- 14.3/14.3 MB 4.9 MB/s eta 0:00:00
    Installing collected packages: mysql-connector-python
    Successfully installed mysql-connector-python-9.0.0

    C:\Apps\.Developer\CMDer Mini\content
    λ
"""

print("-----------------------------------------------")

# Test MySQL Connector
import mysql.connector

print(mysql)
# <module 'mysql' from 'C:\\Users\\Builder\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\mysql\\__init__.py'>

print("-----------------------------------------------")

# Create a connection to a database
mydb = mysql.connector.connect(
  host="localhost",
  user="mysql",
  password="mysql"
)
print(mydb)
# <mysql.connector.connection.MySQLConnection object ar 0x016645F0>
# <mysql.connector.connection_cext.CMySQLConnection object at 0x0000015C8E40F7D0>

print("-----------------------------------------------")

# Criando variável para salvar informações de conexão
mycursor = mydb.cursor()
print(mycursor)
# CMySQLCursor: (Nothing executed yet)

print("-----------------------------------------------")

# Drop a database in MySQL
def deletarDatabase(database):
  try:
    # mycursor.execute("drop DATABASE mydatabase")
    mycursor.execute("drop DATABASE {}".format(database))
    print(f"Base de dados \"{database}\" deletada!")
  except:
    print(f"Base de dados \"{database}\" não deletada!")

# deletarDatabase('mydatabase')
# Base de dados "mydatabase" não deletada!

print("Teste de rotina \"deletarDatabase()\" OK!, Comentada")

print("-----------------------------------------------")

# Create a database in MySQL
def criarDatabase(database):
  try:
    # mycursor.execute("CREATE DATABASE mydatabase")
    mycursor.execute("create DATABASE {}".format(database))
    print(f"Base de dados \"{database}\" criada com sucesso!")
  except:
    print(f"Base de dados \"{database}\" não criada!")

# Testando criar uma base de dados que já existe
# criarDatabase('sakila')
# Base de dados "sakila" não criada!

# Criar uma base de dados que não existe
# criarDatabase('mydatabase')
# Base de dados "mydatabase" criada com sucesso!

#If this page is executed with no error, you have successfully created a database.
print("Teste de rotina \"criarDatabase()\" OK!, Comentada")

print("-----------------------------------------------")

# Check if a database exist
def checkDatabase():
  mycursor.execute("SHOW DATABASES")
  for base_de_dados in mycursor:
    print(base_de_dados)

# checkDatabase()
print("Teste de rotina \"checkDatabase()\" OK!, Comentada")

# ('information_schema',)
# ('mydatabase',)
# ('mysql',)
# ('performance_schema',)
# ('sakila',)
# ('sys',)
# ('world',)

print("-----------------------------------------------")

# Drop a table
def deletarTabela():
  import mysql.connector

  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()

  try:
    mycursor.execute("drop TABLE customers")
    print("Tabela deletada!")
  except:
    print("Tabela não deletada!")

# deletarTabela()
print("Teste de rotina \"deletarTabela()\" OK!, Comentada")

#If this page is executed with no error, you have successfully created a table named "customers".

print("-----------------------------------------------")

# Create a table
def criarTabela():
  import mysql.connector

  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()

  try:
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    print("Tabela criada com sucesso")
  except:
    print("Tabela não criada")

# criarTabela()
print("Teste de rotina \"criarTabela()\" OK!, Comentada")

#If this page is executed with no error, you have successfully created a table named "customers".


print("-----------------------------------------------")

# Check if a table exist
def listarTabelas(database):
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    # database="mydatabase"
    database=f"{database}"
  )
  mycursor = mydb.cursor()
  try:
    mycursor.execute("SHOW TABLES")
    print("Comando realizado com sucesso!\n")

    for x in mycursor:
      print(x)
  except:
    print("Erro")

# listarTabelas('mydatabase')
# ('customers',)

print("Teste de rotina \"listarTabelas()\" OK!, Comentada")

print("-----------------------------------------------")

# Create primary key when creating a table
def criarPrimaryKey(database):
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    # database="mydatabase"
    database=f"{database}"
  )
  mycursor = mydb.cursor()
  try:
    # mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    mycursor.execute("alter TABLE customers add column id INT AUTO_INCREMENT PRIMARY KEY")
    print("Comando realizado com sucesso!\n")
  except:
    print("Error")

# criarPrimaryKey('mydatabase')
#If this page is executed with no error, the table "customers" now has a primary key
print("Teste de rotina \"criarPrimaryKey()\" OK!, Comentada")


print("-----------------------------------------------")

# Insert a record in a table
def insert():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )

  mycursor = mydb.cursor()
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = ("John", "Highway 21")

  try:
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
  except:
    mydb.rollback()
    print("Error")

# insert()
print("Teste de rotina \"insert()\" OK!, Comentada")

print("-----------------------------------------------")

# Insert multiple rows
def MultipleRowsInsert():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )

  mycursor = mydb.cursor()
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
  ]

  try:
    # mycursor.execute(sql, val)
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "records was inserted.")
  except:
    mydb.rollback()
    print("Error")

# MultipleRowsInsert()
print("Teste de rotina \"MultipleRowsInsert()\" OK!, Comentada")


print("-----------------------------------------------")

# Get inserted ID
def insertReturnLastID():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )

  mycursor = mydb.cursor()
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = ("Michelle", "Blue Village")

  try:
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"1 record inserted, ID: {mycursor.lastrowid}")
  except:
    mydb.rollback()
    print("Error")

# insertReturnLastID()
print("Teste de rotina \"insertReturnLastID()\" OK!, Comentada")

print("-----------------------------------------------")

# Select all records from a table
def select():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# select()
print("Teste de rotina \"select()\" OK!, Comentada")

# ('John', 'Highway 21', 1)
# ('Peter', 'Lowstreet 4', 2)
# ('Amy', 'Apple st 652', 3)
# ('Hannah', 'Mountain 21', 4)
# ('Michael', 'Valley 345', 5)
# ('Sandy', 'Ocean blvd 2', 6)
# ('Betty', 'Green Grass 1', 7)
# ('Richard', 'Sky st 331', 8)
# ('Susan', 'One way 98', 9)
# ('Vicky', 'Yellow Garden 2', 10)
# ('Ben', 'Park Lane 38', 11)
# ('William', 'Central st 954', 12)
# ('Chuck', 'Main Road 989', 13)
# ('Viola', 'Sideway 1633', 14)
# ('Michelle', 'Blue Village', 15)

print("-----------------------------------------------")

# Select only some of the columns in a table
def selectColumns():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )

  mycursor = mydb.cursor()
  try:
    mycursor.execute("SELECT name, address FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectColumns()
print("Teste de rotina \"selectColumns()\" OK!, Comentada")

print("-----------------------------------------------")

# Use the fetchone() method to fetch only one row in a table
def selectFetchoneMethod():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    mycursor.execute("SELECT * FROM customers")
    # If you are only interested in one row, you can use the fetchone() method.
    # The fetchone() method will return the first row of the result:
    myresult = mycursor.fetchone()
    print(myresult)
  except:
    print("Error")

# selectFetchoneMethod()
print("Teste de rotina \"selectFetchoneMethod()\" OK!, Comentada")
# ('John', 'Highway 21', 1)

print("-----------------------------------------------")

# Select with a filter
def selectWithFilter():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

selectWithFilter()
# print("Teste de rotina \"selectWithFilter()\" OK!, Comentada")
# ('Ben', 'Park Lane 38', 11)

print("-----------------------------------------------")

# Wildcards characters
def selectWithWildcardCharacters():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "SELECT * FROM customers WHERE address Like '%way%'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectWithWildcardCharacters()
print("Teste de rotina \"selectWithWildcardCharacters()\" OK!, Comentada")
# ('John', 'Highway 21', 1)
# ('Susan', 'One way 98', 9)
# ('Viola', 'Sideway 1633', 14)

print("-----------------------------------------------")

# Prevent SQL injection
def selectPreventSQLInjection():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "SELECT * FROM customers WHERE address = %s"
    # adr = ("Yellow Garden 2") # Error
    adr = ("Yellow Garden 2",)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

selectPreventSQLInjection()
# print("Teste de rotina \"selectPreventSQLInjection()\" OK!, Comentada")
# ('Vicky', 'Yellow Garden 2', 10)

print("-----------------------------------------------")

# Sort the result of a table alphabetically
def selectWithOrderBy():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "SELECT * FROM customers ORDER BY name"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectWithOrderBy()
print("Teste de rotina \"selectWithOrderBy()\" OK!, Comentada")
# ('Amy', 'Apple st 652', 3)
# ('Ben', 'Park Lane 38', 11)
# ('Betty', 'Green Grass 1', 7)
# ('Chuck', 'Main Road 989', 13)
# ('Hannah', 'Mountain 21', 4)
# ('John', 'Highway 21', 1)
# ('Michael', 'Valley 345', 5)
# ('Michelle', 'Blue Village', 15)
# ('Peter', 'Lowstreet 4', 2)
# ('Richard', 'Sky st 331', 8)
# ('Sandy', 'Ocean blvd 2', 6)
# ('Susan', 'One way 98', 9)
# ('Vicky', 'Yellow Garden 2', 10)
# ('Viola', 'Sideway 1633', 14)
# ('William', 'Central st 954', 12)

print("-----------------------------------------------")

# Sort the result in a descending order (reverse alphabetically)
def selectWithOrderByDesc():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "SELECT * FROM customers ORDER BY name DESC"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectWithOrderByDesc()
print("Teste de rotina \"selectWithOrderByDesc()\" OK!, Comentada")
# ('William', 'Central st 954', 12)
# ('Viola', 'Sideway 1633', 14)
# ('Vicky', 'Yellow Garden 2', 10)
# ('Susan', 'One way 98', 9)
# ('Sandy', 'Ocean blvd 2', 6)
# ('Richard', 'Sky st 331', 8)
# ('Peter', 'Lowstreet 4', 2)
# ('Michelle', 'Blue Village', 15)
# ('Michael', 'Valley 345', 5)
# ('John', 'Highway 21', 1)
# ('Hannah', 'Mountain 21', 4)
# ('Chuck', 'Main Road 989', 13)
# ('Betty', 'Green Grass 1', 7)
# ('Ben', 'Park Lane 38', 11)
# ('Amy', 'Apple st 652', 3)

print("-----------------------------------------------")

# Delete records from an existing table
def deleteRecords():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
  except:
    print("Error")

# deleteRecords()
print("Teste de rotina \"deleteRecords()\" OK!, Comentada")
# 1 record(s) deleted

print("-----------------------------------------------")

# Prevent SQL injection
def deleteRecordsPreventSQLinjection():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "DELETE FROM customers WHERE address = %s"
    adr = ("Yellow Garden 2",)
    mycursor.execute(sql, adr)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
  except:
    print("Error")

# deleteRecordsPreventSQLinjection()
print("Teste de rotina \"deleteRecordsPreventSQLinjection()\" OK!, Comentada")
# 1 record(s) deleted

print("-----------------------------------------------")

# Delete an existing table
def dropTable(database, table):
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database=f"{database}"
  )
  mycursor = mydb.cursor()
  try:
    sqltmp = "create table customersTMP as select * from mydatabase.customers"
    mycursor.execute(sqltmp)
    mydb.commit()
    print("Tabela temporária criada!")
    try:
      sql = f"DROP TABLE {table}"
      mycursor.execute(sql)
      mydb.commit()
      print("Tabela temporária deletada!")
    except:
      mydb.rollback()
      print("Error ao deletar tabela temporária")
  except:
    mydb.rollback()
    print("Erro ao criar tabela temporária!")

# dropTable('mydatabase', 'customersTMP')
print("Teste de rotina \"dropTable()\" OK!, Comentada")
# If this page was executed with no error(s), you have successfully deleted the "customers" table.

print("-----------------------------------------------")

# Delete a table if it exist
def dropTableWithIfExist(database, table):
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database=f"{database}"
  )
  mycursor = mydb.cursor()
  try:
    sqltmp = "create table customersTMP as select * from mydatabase.customers"
    mycursor.execute(sqltmp)
    mydb.commit()
    print("Tabela temporária criada!")
    try:
      # sql = "DROP TABLE IF EXISTS customers"
      sql = f"DROP TABLE IF EXISTS {table}"
      mycursor.execute(sql)
      mydb.commit()
      print("Tabela temporária deletada!")
    except:
      mydb.rollback()
      print("Error ao deletar tabela temporária")
  except:
    mydb.rollback()
    print("Erro ao criar tabela temporária!")

# dropTableWithIfExist('mydatabase', 'customersTMP')
print("Teste de rotina \"dropTableWithIfExist()\" OK!, Comentada")
# If this page was executed with no error(s), you have successfully deleted the "customers" table.

print("-----------------------------------------------")

# Update existing records in a table
def updateTable():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
  except:
    mydb.rollback()
    print("Error")

# updateTable()
print("Teste de rotina \"updateTable()\" OK!, Comentada")
# 1 record(s) affected

print("-----------------------------------------------")

# Prevent SQL injection
def updateTablePreventSQLinjection():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "UPDATE customers SET address = %s WHERE address = %s"
    val = ("Valley 345", "Canyon 123")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
  except:
    mydb.rollback()
    print("Error")

# updateTablePreventSQLinjection()
print("Teste de rotina \"updateTablePreventSQLinjection()\" OK!, Comentada")
# 1 record(s) affected

print("-----------------------------------------------")

# Limit the number of records returned from a query
def selectWithLimiteResult():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    mycursor.execute("SELECT * FROM customers LIMIT 5")
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectWithLimiteResult()
print("Teste de rotina \"selectWithLimiteResult()\" OK!, Comentada")
# ('John', 'Highway 21', 1)
# ('Peter', 'Lowstreet 4', 2)
# ('Amy', 'Apple st 652', 3)
# ('Michael', 'Valley 345', 5)
# ('Sandy', 'Ocean blvd 2', 6)

print("-----------------------------------------------")

# Limit the number of records returned from a query 'Another Position'
def selectWithLimiteResultOffSet():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2") # Pule os 2 primeiros e retorne os próximos 5 registros
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectWithLimiteResultOffSet()
print("Teste de rotina \"selectWithLimiteResultOffSet()\" OK!, Comentada")
# ('Amy', 'Apple st 652', 3)
# ('Michael', 'Valley 345', 5)
# ('Sandy', 'Ocean blvd 2', 6)
# ('Betty', 'Green Grass 1', 7)
# ('Richard', 'Sky st 331', 8)

print("-----------------------------------------------")

# Combine rows from two or more tables, based on a related column between them

r"""
Pré-Requisitos:
Criar as seguintes tabelas:

create table mydatabase.users(
	id   int NOT NULL AUTO_INCREMENT,
    name varchar(255) DEFAULT NULL,
    fav  varchar(255) DEFAULT NULL,
    PRIMARY KEY (id)
);

# truncate table mydatabase.users;

insert into mydatabase.users values(1, 'John', 154);
insert into mydatabase.users values(2, 'Peter', 154);
insert into mydatabase.users values(3, 'Amy', 155);
insert into mydatabase.users (id, name) values(4, 'Hannah');
insert into mydatabase.users (id, name) values(5, 'Michael');

commit;

select * from mydatabase.users;

# ---

create table mydatabase.products(
	id   int NOT NULL AUTO_INCREMENT,
    name varchar(255) DEFAULT NULL,    
    PRIMARY KEY (id)
);

insert into mydatabase.products values(1, 'Chocolate Heaven');
insert into mydatabase.products values(2, 'Tasty Lemons');
insert into mydatabase.products values(3, 'Vanilla Dreams');

commit;

select * from mydatabase.products;
"""
def selectWithJoin():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      INNER JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectWithJoin()
print("Teste de rotina \"selectWithJoin()\" OK!, Comentada")
# ('John', 'Chocolate Heaven')
# ('Peter', 'Chocolate Heaven')
# ('Amy', 'Tasty Lemons')

print("-----------------------------------------------")

# LEFT JOIN
def selectWithLeftJoin():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      LEFT JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectWithLeftJoin()
print("Teste de rotina \"selectWithLeftJoin()\" OK!, Comentada")
# ('John', 'Chocolate Heaven')
# ('Peter', 'Chocolate Heaven')
# ('Amy', 'Tasty Lemons')
# ('Hannah', None)
# ('Michael', None)

print("-----------------------------------------------")

# RIGHT JOIN
def selectWithRighttJoin():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="mysql",
    password="mysql",
    database="mydatabase"
  )
  mycursor = mydb.cursor()
  try:
    sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      RIGHT JOIN products ON users.fav = products.id"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
      print(x)
  except:
    print("Error")

# selectWithRighttJoin()
print("Teste de rotina \"selectWithRighttJoin()\" OK!, Comentada")
# ('Peter', 'Chocolate Heaven')
# ('John', 'Chocolate Heaven')
# ('Amy', 'Tasty Lemons')
# (None, 'Vanilla Dreams')

print("-----------------------------------------------")