from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PickleType
# from sqlalchemy.orm import sessionmaker

from base import Base

class StoreLocation(Base):

    def __init__(self, storeName, storeCode, storeAddress, storeMenu, createdBy = None):
        self.storeName = storeName
        self.storeCode = storeCode
        self.storeAddress = storeAddress
        self.storeMenu = storeMenu
        self.createdBy = createdBy
    

    def __repr__(self):
        return "Name: {0}\nCode: {1}\nAddress: {2}\nCreated by: {3}".format(self.storeName, self.storeCode, self.storeAddress, self.createdBy)

    __tablename__ = 'StoreLocation'

    storeID = Column(Integer, primary_key=True)
    storeName = Column(String)
    storeCode = Column(String)
    storeAddress = Column(String)
    # TODO: store an array in the menu column
    storeMenu = Column(PickleType)
    createdBy = Column(String)

