import sqlite3

db_connect = sqlite3.connect('d13.sqlite3')

db_cursor = db_connect.cursor()


def create_users():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, full_name TEXT, phone TEXT, telegram_id INTEGER
        )
    """)
    db_connect.commit()


def create_table_product():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price REAL,
        photo TEXT)
    """)


create_table_product()
create_users()

def create_table_orders():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        user_id INTEGER)
    """)


create_table_orders()


async def db_insert_product(title, price, photo_id):
    db_cursor.execute("""
            INSERT INTO product (title, price, photo)
            VALUES(?, ?, ?)""", (title, price, photo_id))
    db_connect.commit()


async def insert_orders(product_id, user_id):
    db_cursor.execute("""
            INSERT INTO orders (product_id, user_id)
            VALUES(?, ?)""", (product_id, user_id))
    db_connect.commit()


def db_get_all_products():
    products = db_cursor.execute("""
        SELECT * FROM product
    """).fetchall()
    return products
#
#
# async def db_get_all_orders(user_id):
#     orders = db_cursor.execute("""
#         SELECT * FROM orders WHERE user_id=?
#     """, (user_id,)).fetchall()
#
#     products = []
#     for order in orders:
#         product = db_cursor.execute("""
#         SELECT * FROM product WHERE id=?
#         """, (order[1],)).fetchone()
#
#         products.append(product)
#
#     user = db_cursor.execute("""
#         SELECT * FROM users WHERE telegram_id=?
#     """, (user_id,)).fetchone()
#     return user, products
#

def db_create_korzina():
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Korzina (

    id INTEGER PRIMARY KEY,
    title TEXT,
    price INTEGER,
    quantity INTEGER)
    """)


db_create_korzina()


async def db_insert_korzina(title):
    db_cursor.execute("""
            INSERT INTO product (title)
            VALUES(?)""", title)
    db_connect.commit()


db_create_korzina()


def db_create_buys():
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Buys (
    id INTEGER PRIMARY KEY,
    title TEXT,
    price INTEGER,
    quantity INTEGER,
    photo TEXT)
    """)


db_create_buys()


async def db_insert_buys(title):
    db_cursor.execute("""
            INSERT INTO product (title)
            VALUES(?)""", title)
    db_connect.commit()


db_create_buys()