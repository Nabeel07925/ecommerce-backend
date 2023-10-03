import random
from datetime import datetime

import mysql.connector
import csv

config = {
    "host": "104.199.205.12",
    "user": "admin",
    "password": "SkoogEarth123!",
    "database": "public",
}


def get_brand_id(cur, con, brand_name):
    cur.execute('select * from public.brand where name = "{}"'.format(brand_name))
    brand = cur.fetchone()
    brand_id = brand[1] if brand else None
    if not brand_id:
        cur.execute('''INSERT INTO brand (name) VALUES ("{}")'''.format(brand_name))
        brand_id = cur.lastrowid
        con.commit()

    return brand_id


def get_product_id(cur, con, product_name, brand_id, category_id):
    cur.execute('select * from public.product where name = "{}"'.format(product_name))
    product = cur.fetchone()
    product_id = product[3] if product else None
    if not product_id:
        cur.execute('''INSERT INTO product (name, brand_id, category_id, created_at, updated_at) 
        VALUES ("{}", {}, {}, "{}", "{}")'''.format(product_name, brand_id, category_id, str(datetime.utcnow()), str(datetime.utcnow())))
        product_id = cur.lastrowid
        con.commit()

    return product_id


def get_inventory_id(cur, con, product_id, stock_id, no_of_items, retail_price, invoice_price):
    cur.execute('select * from public.inventory where product_id = "{}"'.format(product_id))
    inventory = cur.fetchone()
    inventory_id = inventory[7] if inventory else None
    if not inventory_id:
        cur.execute('''INSERT INTO inventory (product_id, stock_id, no_of_items_available, 
        retail_price, invoice_price, created_at, updated_at) 
        VALUES ({}, {}, {}, {}, {}, "{}", "{}")'''.format(product_id, stock_id, no_of_items,
                                                          retail_price, invoice_price,
                                                          str(datetime.utcnow()), str(datetime.utcnow())))
        inventory_id = cur.lastrowid
        con.commit()

    return inventory_id


def remove_inventory(cur, con, inventory_id, no_of_items_removed):
    cur.execute('''Select no_of_items_available from public.inventory where id = {}'''.format(inventory_id))
    inventory = cur.fetchone()
    if inventory:
        no_of_items_before = inventory[0]
        cur.execute('''UPDATE public.inventory SET no_of_items_available = {} where id = {}'''.
                    format(no_of_items_before - no_of_items_removed, inventory_id))
        updated_inventory = cur.fetchone()
        if cur.rowcount:
            con.commit()
            return True
    return False


def add_order(cur, con, inventory_id, retail_price, invoice_price):
    # in real scenarios there will of course be multiple sorts of items in one order but for now there would just be one
    no_of_items = random.randint(1, 5)
    cur.execute('''INSERT INTO public.order (state, shipping_charges, total_amount, 
    total_cost, created_at, updated_at) 
    VALUES ("{}", {}, {}, {}, "{}", "{}")'''.format("completed", 10.0, retail_price * no_of_items,
                                                      invoice_price * no_of_items,
                                                      str(datetime.utcnow()), str(datetime.utcnow())))
    order_id = cur.lastrowid
    if order_id:
        cur.execute('''INSERT INTO public.order_item (no_of_items, inventory_id, 
        order_id, 
        created_at, updated_at) 
        VALUES ({}, {}, {}, "{}", "{}")'''.format(no_of_items, inventory_id,
                                                  order_id,
                                                  str(datetime.utcnow()), str(datetime.utcnow())))
        if cur.lastrowid:
            con.commit()
            remove_inventory(cur=cur,
                             con=con,
                             inventory_id=inventory_id,
                             no_of_items_removed=no_of_items)
            return True

    return False


if __name__ == '__main__':
    cnx = mysql.connector.connect(user='admin', password='SkoogEarth123!',
                                  host='104.199.205.12',
                                  database='public')
    cur = cnx.cursor()
    cur.execute('select * from public.product_category where code = "CLOTHING"')
    category = cur.fetchone()
    category_id = category[2] if category else None
    if not category:
        cur.execute('''INSERT INTO product_category (name, code) VALUES ("{}", "{}")'''.format('clothing', 'CLOTHING'))
        cnx.commit()
        category_id = cur.lastrowid

    with open('data/clothing_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            try:
                if line_count == 0:
                    cols = row
                    brands_index = cols.index('Brand')
                    product_name_index = cols.index('product_name')
                    price_index = cols.index('price_original')
                    print('Column names are {} {} {}'.format(brands_index, product_name_index, price_index))
                    line_count += 1
                else:
                    brand_id = get_brand_id(cur, cnx, row[brands_index])
                    product_id = get_product_id(cur=cur,
                                                con=cnx,
                                                product_name=row[product_name_index],
                                                brand_id=brand_id,
                                                category_id=category_id)
                    product_price = float(row[price_index])
                    invoice_price = product_price - (product_price * 0.30)
                    inventory_id = get_inventory_id(cur=cur,
                                                    con=cnx,
                                                    product_id=product_id,
                                                    stock_id=1,
                                                    no_of_items=50000,
                                                    retail_price=product_price,
                                                    invoice_price=invoice_price
                                                    )

                    order_placed = add_order(cur=cur,
                                             con=cnx,
                                             inventory_id=inventory_id,
                                             retail_price=product_price,
                                             invoice_price=invoice_price)
            except Exception as e:
                print(e)
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'All orders processed')

    cur.close()
    cnx.close()