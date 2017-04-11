from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Enum


Base = declarative_base()


# region # Enums

class ChocolateType(Enum):
    Milk = 'milk'
    Dark = 'dark'
    White = 'white'


class PackageSize(Enum):
    Normal = 'normal'
    Small = 'small'
    Unit = 'unit'
    Pack = 'pack'

# endregion


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    sku = Column(String, unique=True)
    name = Column(String)
    barcode = Column(String)
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_on': type
    }


class Candy(Product):
    __tablename__ = 'candy'

    id = Column(Integer, ForeignKey(Product.__tablename__ + '.id', ondelete='CASCADE'), primary_key=True)
    package_size = Column(String, default=PackageSize.Normal)
    chocolate_type = Column(String, default=None)
    contents = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': __tablename__
    }


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, default=0)

    product_sku = Column(String, ForeignKey(Product.__tablename__ + '.sku'))
