import sqlalchemy as sql
from sqlalchemy import event, engine
from Mapping import *

#region # Setup and globals


engine = sql.create_engine('sqlite:///sweetbox.db', echo=True)
Base.metadata.create_all(engine)

Session = sql.orm.sessionmaker(bind=engine)
session = Session()


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Handles event fired when connecting to DB, sets up SQLite
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

#endregion

#region # Getters


def get_product_with_sku(sku):
    return session.query(Product).filter(Product.sku == sku)


def get_product_with_barcode(barcode):
    return session.query(Product).filter(Product.barcode == barcode)


def get_all_products():
    return session.query(Product).all()

#endregion


def add_product(product):
    session.add(product)
    session.commit()


def remove_product_with_sku(sku):
    product = session.query(Product).filter(Product.sku == sku).first()
    session.delete(product)
    session.commit()


def add_product_to_inventory(product, price, quantity):
    existing_product = True if session.query(Product).filter(Product.sku == product.sku).count() > 0 else False
    if not existing_product:
        add_product(product)

    inventory_item = Inventory(price=price, quantity=quantity, product_sku=product.sku)
    session.add(inventory_item)
    session.commit()


def remove_product_with_sku_from_inventory(sku):
    inventory_item = session.query(Inventory).filter(Inventory.product_sku == sku).first()
    session.delete(inventory_item)
    session.commit()


def get_inventory_joined_with_product():
    invproduct, product = session.query(Inventory, Product).join(Product).first()
    print invproduct

def test():
    new_products = [Product(sku='mint_gum_dirol', name='Dirol Mint', barcode='00000000'),
                    Candy(sku='haribo_bears_small', name='Haribo Bears', barcode='00000000', type='candy',
                          package_size=PackageSize.Small, contents='jelly'),
                    Candy(sku='kitkat_white_double', name='KitKat White', barcode='00000000', type='candy',
                          chocolate_type=ChocolateType.White, package_size=PackageSize.Normal)
                    ]
    # for product in new_products:
    #     add_product(product)

    all_products = get_all_products()
    for product in all_products:
        print product

    # remove_product_with_sku('haribo_bears_small')

    add_product_to_inventory(new_products[2], price='100', quantity='2')
    add_product_to_inventory(new_products[0], price='250', quantity='5')
    # remove_product_with_sku_from_inventory('haribo_bears_small')
    get_inventory_joined_with_product()


test()
