from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, PickleType
from OrderTicket import OrderTicket
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
    storeCode = Column(String, unique=True)
    storeAddress = Column(String)
    # TODO: store an array in the menu column
    storeMenu = Column(PickleType)
    createdBy = Column(String)
    orders = relationship(OrderTicket)

    def prettyPrint(self, indent=0):
        for key, value in self.storeMenu.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                self.prettyPrint(value, indent+1)
            else:
                for item in value:
                    print('\t' * (indent+1) + str(item))
                    

    def createOrder(self):
        orderList = []
        print('Creating Order...')
        self.prettyPrint()
        orderNumsStr = input(str("Pick the item numbers for your order (ex: E1,S2,D3): ")).upper().strip()
        orderNumList = orderNumsStr.split(',')
        # Would have been a great place for a switch statement...
        for num in orderNumList:
            num = num.strip()
            if num[0] == 'E':
                for item in self.storeMenu['Entres']:
                    if num == item.itemNumber:
                        orderList.append(item)
            elif num[0] == 'S':
                for item in self.storeMenu['Sides']:
                    if num == item.itemNumber:
                        orderList.append(item)
            elif num[0] == 'D':
                for item in self.storeMenu['Desserts']:
                    if num == item.itemNumber:
                        orderList.append(item)
        orderObj = OrderTicket(orderList, self.storeCode)
        # print(orderObj)
        return orderObj
    
    def createTestOrder(self):
        orderList = []
        orderNumList = ["E1","S2","D3"]
        for num in orderNumList:
            num = num.strip()
            if num[0] == 'E':
                for item in self.storeMenu['Entres']:
                    if num == item.itemNumber:
                        orderList.append(item)
            elif num[0] == 'S':
                for item in self.storeMenu['Sides']:
                    if num == item.itemNumber:
                        orderList.append(item)
            elif num[0] == 'D':
                for item in self.storeMenu['Desserts']:
                    if num == item.itemNumber:
                        orderList.append(item)
        orderObj = OrderTicket(orderList, self.storeCode)
        # print(orderObj)
        return orderObj