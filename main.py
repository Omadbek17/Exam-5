#Exam number-5 N-42 group
#Omadbek Qosimov
from psycopg2._psycopg import cursor


#1 Masala
# import psycopg2
#
# conn = psycopg2.connect(
#     dbname="postgres",
#     user="postgres",
#     password="omad2006",
#     host="localhost",
#     port="5432"
# )
# 
# cur = conn.cursor()
#
# create_table_query = """
#     CREATE TABLE IF NOT EXISTS Product(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255) NOT NULL,
#         price NUMERIC NOT NULL,
#         color VARCHAR(50) default 'white',
#         image VARCHAR(255)
#         );
# """
#
# cur.execute(create_table_query)
#
# conn.commit()
#
# cur.close()
# conn.close()
#
#


#2 Masala

# products = []
# def insert_product(product):
#     products.append(product)
#     print("Product successfully inserted")
#
#
# def select_all_products():
#     if not products:
#         print("There are no products.")
#     else:
#         print("All products:")
#         for product in products:
#             print(product)
#
#
# def update_product(old_product, new_product):
#     if old_product in products:
#         index = products.index(old_product)
#         products[index] = new_product
#         print("Product updated.")
#     else:
#         print("We can't find that product.")
#
#
# def delete_product(product):
#     if product in products:
#         products.remove(product)
#         print("Product successfully deleted.")
#     else:
#         print("There are no products.")
#
#
# insert_product("Iphone 15")
# insert_product("Mobilephones")
# select_all_products()
# update_product("Mobilephone", "Laptops")
# delete_product("Iphone 15")
# select_all_products()


#3 Masala

# class Alphabet:
#     def __init__(self):
#         self.letters = 'abcdefghijklmnopqrstuvwxyz'
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.letters):
#             letter = self.letters[self.index]
#             self.index += 1
#             return letter
#         else:
#             raise StopIteration
#
# alphabet = Alphabet()
#
# for letter in alphabet:
#     print(letter)


#4 Masala
#
# import threading
# import time
#
# def func1():
#     for i in range(1,6):
#         print(f'Number => {i}')
#         time.sleep(1)
#
# thread1 = threading.Thread(target=func1)
# thread1.start()
#
# def func2():
#     for i in 'ABCDE':
#         print(f'Character => {i}')
#         time.sleep(1)
#
#
# thread1 = threading.Thread(target=func1)
# thread2 = threading.Thread(target=func2)
# thread2.start()
#
# thread2.join()
# start_time = time.time()
#


#5 Misol
#
# class Product:
#     def __init__(self, name, price, color, image):
#         self.name = name
#         self.price = price
#         self.color = color
#         self.image = image
#
#
#     def save(self):
#         insert_table_query = "INSERT INTO Product (name, price, color, image) VALUES(%s, %s, %s, %s)"
#         print("Product bazaga saqlandi:", self.name, self.price, self.color, self.image)
#
# product = Product(name='Victus', price='700', color='Black', image='https://t.me/qosimoff_701')
# product.save()
#



#6 Masala

# import psycopg2
#
# class DbConnect:
#     def __init__(self, dbname, user, password, host, port):
#         self.dbname = dbname
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             dbname=self.dbname,
#             user=self.user,
#             password=self.password,
#             host=self.host,
#             port=self.port
#         )
#         self.cur = self.conn.cursor()
#         return self.conn, self.cur
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.conn.commit()
#         self.cur.close()
#         self.conn.close()
#
#
# with DbConnect('postgres', 'user', 'omad2006', 'localhost', '5432') as (conn, cur):
#
#     cur.execute("SELECT * FROM Product")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
