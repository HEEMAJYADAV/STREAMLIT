#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
conn = sqlite3.connect("Ex.db")
cur = conn.cursor()

cur.execute('CREATE TABLE STAFF(NAME CHAR(20),AGE INTEGER)')
conn.execute('CREATE TABLE STUDENT(NAME CHAR(20),AGE INTEGER)')


# In[1]:


import sqlite3
conn = sqlite3.connect("Example.db")
cur = conn.cursor()

cur.execute('insert into STAFF values("SHILPA",34)')
cur.execute('insert into STAFF values("CHITHRA",30)')

cur.execute('insert into STUDENT values("KRISHNA",20)')
cur.execute('insert into STUDENT values("SHAM",21)')

info1 = ("Shiva",22)
info2 = ("Ramadevi",33)

cur.execute('insert into STUDENT(NAME,AGE) VALUES(?,?)',info1)
cur.execute('insert into STAFF(NAME,AGE) VALUES(?,?)',info2)

x = cur.execute('select *from STAFF')
for i in x:
    print(i)

y = cur.execute('select *from STUDENT')    
for i in y:
    print(i)
    
print("Done")    


# In[2]:


import sqlite3

con = sqlite3.connect(":memory:") # create DB in RAM instead of Hard Disk
cur = con.cursor()
cur.execute("create table people (name_last, age)")
who = "PAP"
age =24
# This is the qmark style:
cur.execute("insert into people values (?, ?)", (who, age))
# And this is the named style:
x = cur.execute("select * from people where name_last=:who and age=:age", {"who": who, "age": age})
for i in x:
    print(i)


# In[3]:


import sqlite3
conn = sqlite3.connect('class1.db')
#create
print ("Opened database successfully")
conn.execute('''CREATE TABLE COMPANY
            (ID INT PRIMARY KEY,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50),
            SALARY REAL);''')
print ("Table created successfully")


# In[4]:


import sqlite3
conn = sqlite3.connect('class1.db')
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Paul', 32, 'California', 20000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Allen', 25, 'Texas aaa', 15000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'Teddy', 23, 'Norway main', 20000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
conn.commit()
print("Records created successfully")


# In[5]:


import sqlite3
conn = sqlite3.connect('class1.db')
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
    print ("ID = ", row[0])
    print ("NAME = ", row[1])
    print ("ADDRESS = ", row[2])
    print ("SALARY = ", row[3], "\n")
print ("Operation done successfully")


# In[6]:


import sqlite3
conn = sqlite3.connect('class1.db')
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
print ("ID\t NAME\t ADDRESS\t SALARY")
for row in cursor:
    print (row[0],end='\t')
    print (row[1],end='\t')
    print (row[2],end='\t')
    print (row[3],end='\t')
    print ( )
print ("Operation done successfully")


# In[7]:


import sqlite3
conn = sqlite3.connect('class1.db')
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)


# In[8]:


import sqlite3
conn = sqlite3.connect('class1.db')
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
print ("ID\t NAME\t ADDRESS\t SALARY")
for row in cursor:
    print (row[0],end='\t')
    print (row[1],end='\t')
    print (row[2],end='\t')
    print (row[3],end='\t')
    print ( )
print ("Operation done successfully")


# In[9]:


import sqlite3
con=sqlite3.connect("example1.db")
cur=con.cursor()

con.execute('''CREATE TABLE supplier_groups(group_id integer PRIMARY KEY, group_name text NOT NULL)''')
con.execute('''CREATE TABLE suppliers(supplier_id   INTEGER PRIMARY KEY, supplier_name TEXT NOT NULL,
group_id INTEGER NOT NULL,FOREIGN KEY (group_id) REFERENCES supplier_groups(group_id))''')


# In[10]:


import sqlite3
con=sqlite3.connect("example1.db")
cur=con.cursor()

con.execute("insert into supplier_groups values(1,'abc')")

con.execute("insert into supplier_groups values(2,'pqr')")

con.execute("insert into supplier_groups values(3,'xyz')")

x=con.execute("select * from supplier_groups")
a = x.fetchone()
print(a)
x=con.execute("select * from supplier_groups")
b = x.fetchall()
print(b)
x=con.execute("select * from supplier_groups")
z = x.fetchmany(2)
print(z)


# In[ ]:




