import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Keeru@143')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute('create database Inventory_Management')
cur.execute('use Inventory_Management')
# Create the 'manufacture' table
cur.execute('CREATE TABLE manufacture (manufacture_id INTEGER PRIMARY KEY, item_name VARCHAR(20),company varchar(20),item_color VARCHAR(20),quantity INTEGER(4),defective_items INTEGER(4))')

# Create the 'goods' table
cur.execute('CREATE TABLE goods (goods_id INTEGER(4) PRIMARY KEY, manufacture_id INTEGER, manufacture_date DATE,FOREIGN KEY(manufacture_id) REFERENCES manufacture(manufacture_id))')

# Create the 'purchase' table
cur.execute('CREATE TABLE purchase (purchase_id INTEGER(4) PRIMARY KEY,  store_name varchar(20),purchase_amount FLOAT, purchase_date DATE)')

# Create the 'sale' table
cur.execute('CREATE TABLE sale (sale_id INTEGER(4) PRIMARY KEY,store_name VARCHAR(30),sale_date DATE,goods_id INTEGER(4), profit_margin FLOAT,FOREIGN KEY(goods_id) REFERENCES goods(goods_id))')

a='insert into manufacture(manufacture_id ,item_name ,company,item_color ,quantity ,defective_items) values (%s,%s,%s,%s,%s,%s)'
entrie1 = (1, 'wooden chair','GARUD ENTERPRISES' ,'brown', 100, 0), (3, 'wooden table','SS EXPORT' 'brown', 50, 1),(2, 'red toy','F3 TOYS','red', 200, 0),(4,'shirt','ADIDAS','black',300,1)
cur.executemany(a,entrie1)
mydb.commit()
#Insert multiple entries to the 'goods' table
b='insert into goods(goods_id , manufacture_id , manufacture_date)values (%s,%s,%s)'
entrie2 = (1, 1, '2023-04-20'),(2, 1, '2023-04-22'),(3, 2, '2023-04-25'),(4, 3, '2023-04-26')
cur.executemany(b,entrie2)
mydb.commit()
# Insert multiple entries to the 'purchase' table
c='insert into purchase(purchase_id , store_name,purchase_amount,purchase_date)values(%s,%s,%s,%s)'
entrie3 = (1, 'ORay', 500, '2023-04-21'), (2, 'MyKids', 1000, '2023-04-22'),(3, 'OnlineMart', 750, '2023-04-23')
cur.executemany(c,entrie3)
mydb.commit()
# Insert multiple entries to the 'sale' table
d='INSERT INTO sale(sale_id ,store_name ,sale_date,goods_id , profit_margin )values(%s,%s,%s,%s,%s)'
entrie4 = (1, 'MyCare', '2023-04-01', 1, 100),(2, 'ORay', '2023-04-03', 2, 50),(3, 'MyKids', '2023-04-05', 3, 75),(4, 'OnlineMart', '2023-04-06', 4, 80)
cur.executemany(d,entrie4)
mydb.commit()

#Queries
a1='DELETE FROM purchase WHERE item_name = "shirt" AND purchase_date = "2023-04-01" AND store_name = "ORay"'
cur.execute(a1)
mydb.commit()


a2='UPDATE manufacture SET quantity = 500 WHERE item_color = "red" AND manufacture_id IN (SELECT manufacture_id FROM goods WHERE goods_id IN (SELECT goods_id FROM sale WHERE store_name = "MyKids")'
cur.execute(a2)
mydb.commit()


a3='SELECT * FROM  goods JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE item_name = "wooden chair" AND manufacture_date< "2023-05-01"'
cur.execute(a3)
rows=cur.fetchall()
for x in rows:
    print(x)
mydb.commit()

a4='SELECT sale.profit_margin FROM sale JOIN goods ON sale.goods_id = goods.goods_id JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id JOIN purchase ON goods.purchase_id = purchase.purchase_id WHERE item_name = "wooden table" AND store_name = "MyCare",company = "SS Export"'
cur.execute(a4)
row = cur.fetchone()
print(row[0])
mydb.commit()