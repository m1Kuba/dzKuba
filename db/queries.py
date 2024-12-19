CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT, 
    product_id TEXT,
    photo TEXT
    )
"""


CREATE_TABLE_store_details = """
    CREATE TABLE IF NOT EXISTS store_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    product_id TEXT,
    info_product TEXT
    )
"""

INSERT_store_QUERY = """
    INSERT INTO store (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""


INSERT_store_details_QUERY = """
    INSERT INTO store_details (category, product_id, info_product)
    VALUES (?, ?, ?)
"""

CREATE_TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    collection TEXT
    )
"""
INSERT_collection_products_QUERY = """
    INSERT INTO collection_products (productid, collection)
    VALUES (?, ?)
"""


