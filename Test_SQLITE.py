import sqlite3
conn = sqlite3.connect('baseofdata.db')
c = conn.cursor()

# c.execute("""CREATE TABLE Users
#           (
#           UserID INTEGER PRIMARY KEY AUTOINCREMENT,
#           First TEXT,
#           Last TEXT,
#           EmailID TEXT,
#           Age INTEGER,
#           Number TEXT,
#           City TEXT
#           );
#           """)

# l = [("Joe", "Smith", "joesmith@gmailcom",23,"401-452-4587", "SanFrancisco"),
#     ("Peter", "Parker", "peter20@gmailcom",22,"957-568-1234", "New York"),
#     ("Ross", "Cook", "ross123@gmailcom",26,"902-572-9857", "New York"),
#     ("Emily", "Brown", "emilybrown5@gmailcom",27,"401-999-5252", "Boston"),
#     ("Sasha", "Johnson", "sasha2345 @gmailcom",21,"405-145-2664", "San Jose"),
#     ("Mary", "Hanks", "Maryh@gmailcom",23,"927-444-7563", "Boston")
#     ]

# c.executemany("INSERT INTO Users(First, Last, EmailID, Age, Number, City) VALUES(?,?,?,?,?,?);",l)
# conn.commit()

# c.execute("UPDATE Users SET Number = '405-4747-5588' WHERE First = 'Ross';")

# c.execute("DELETE FROM Users WHERE First = 'Joe' AND Last = 'Smith'; ")

# c.execute("SELECT * FROM Users WHERE Age > '25' AND City = 'Boston';")

# c.execute("SELECT First, EmailID FROM Users WHERE City = 'New York' OR City = 'Boston';")

# c.execute("SELECT MIN(Age) FROM Users;")

# c.execute("SELECT * FROM Users ORDER BY Age;")

# c.execute("SELECT AVG(Age) FROM Users;")

# c.execute("SELECT * FROM Users ORDER BY First;")

# c.execute("SELECT * FROM Users;")

# c.execute("""CREATE TABLE Users
#           (
#           UserID INTEGER PRIMARY KEY AUTOINCREMENT,
#           First TEXT,
#           Last TEXT,
#           EmailID TEXT,
#           Age INTEGER,
#           Number TEXT,
#           City TEXT
#           );
#           """)

# print(c.fetchall())


# c.execute("CREATE TABLE customers(CustomerID INTEGER PRIMARY KEY AUTOINCREMENT, CustomerName TEXT, City TEXT, Country TEXT)")

# c.execute("CREATE TABLE employees(EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT, EmployeeName TEXT, JoiningDate DATE, City TEXT, Country TEXT)")

# c.execute("CREATE TABLE orders(OrderID INTEGER PRIMARY KEY AUTOINCREMENT, CustomerID INTEGER, EmployeeID INTEGER, OrderDate DATE, TotalAmount INTEGER, FOREIGN KEY(CustomerID) REFERENCES customers(CustomerID), FOREIGN KEY(EmployeeID) REFERENCES customers(EmployeeID))")

# clist = [('Steve Liu', 'Nagasaki', 'Japan'),
#         ('Ram Pandey', 'Mumbai', 'India'),
#         ('Mayank Singh', 'Delhi', 'India'),
#         ('James Tang', 'Tokyo', 'Japan'),
#         ('William Johnson', 'San Jose', 'USA'),
#         ('Nick Nelson', 'San Francisco','USA')]

# elist = [('John Taylor', '2016-04-19', 'New York','USA'),
#         ('Bob Williams', '2017-08-25','Boston', 'USA'),
#         ('Anisha Iyer', '2012-04-11', 'Chennai','India'),
#         ('Raj Chawla','2016-02-09', 'Bangalore', 'India'),
#         ('Mark Lee', '2017-01-20', 'Tokyo','Japan')]

# olist = [(6,1,'2019-07-11',110),
#         (5,2, '2018-11-22',85),
#         (4,5,'2019-05-11',98),
#         (3,4,'2017-11-30',45),
#         (2,3, '2018-08-29', 150)]

# c.executemany("INSERT INTO customers(CustomerName, City, Country) VALUES(?,?,?)",clist)
# c.executemany("INSERT INTO employees(EmployeeName, JoiningDate, City, Country) VALUES(?,?,?,?)",elist)
# c.executemany("INSERT INTO orders(CustomerID, EmployeeID, OrderDate, TotalAmount) VALUES(?,?,?,?)", olist)

# conn.commit()

# c.execute("SELECT * FROM customers")
# print(c.fetchall())
# c.execute("SELECT * FROM employees")
# print(c.fetchall())
# c.execute("SELECT * FROM orders")
# print(c.fetchall())


# c.execute("SELECT c.CustomerName,o.TotalAmount FROM orders o JOIN customers c ON o.CustomerID = c.CustomerID")
# print(c.fetchall())
