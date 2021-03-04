from abc import ABCMeta, abstractmethod
from MenuItemFactory import MenuItemFactory
from sqlalchemy import Column, Integer, String

from base import Base

class OrderFacade:
    def __init__(self, items = None):
        self.items = items
        self.theOrder = []
        factory = MenuItemFactory()

        for i in items:
            # set the price for small, medium, large entres
            if i.itemSubType == 'Pizza' or i.itemSubType == 'Pasta' or i.itemSubType == 'Chicken':
                if i.itemSize == 'Chicago':
                    i.price = 25
                elif i.itemSize == 'Large':
                    i.price = 20
                elif i.itemSize == 'Medium':
                    i.price = 15
                elif i.itemSize == 'Small':
                    i.price = 10
                # Create the entre based on the information passed to OrderItem
                entre = factory.create("Entre", i.itemSubType, i.itemSize, i.itemName, i.price, 0)
                self.addToOrder(entre)
            # Handle the side item types:
            elif i.itemSubType == 'Bread' or i.itemSubType == 'Side Salad' or i.itemSubType == 'Dipping Sauce':
                i.price = 5
                side = factory.create("Side", i.itemSubType, 1, i.itemName, i.price, 0)
                self.addToOrder(side)
            
            elif i.itemSubType == 'Cake' or i.itemSubType ==  'Pie' or i.itemSubType == 'Churros':
                i.price = 12
                dessert = factory.create("Dessert", i.itemSubType, i.itemName, i.price, 0)
                self.addToOrder(dessert)
    def Total(self):
        orderTotal = 0
        for item in self.theOrder:
            orderTotal = orderTotal + item.price
        return orderTotal

    def Summary(self):
        for item in self.theOrder:
            print(str(self.theOrder.index(item) + 1) + ": "  + str(item))
        print('\n' + "Order Total: " + "${:3,.2f}".format(self.Total()))
    
    def addToOrder(self, item):
        self.theOrder.append(item)

class OrderItem(Base):
    def __init__(self, itemSubType, itemName, itemSize=None):
        self.itemSubType = itemSubType
        self.itemName = itemName
        self.itemSize = itemSize

    __tablename__ = 'orderItem'

    id = Column(Integer, primary_key=True)
    itemSubType = Column(String)
    itemName = Column(String)
    itemSize = Column(String)

    def __repr__(self):
        return "<orderItem[itemSubType = {0}, itemName = {1}, itemSize = {2}]>".format(self.itemSubType, self.itemName, self.itemSize)