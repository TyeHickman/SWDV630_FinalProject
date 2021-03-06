from abc import ABCMeta, abstractmethod
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import has_inherited_table
from base import Base

class HasIdMixin(object):
    @declared_attr.cascading
    def id(cls):
        if has_inherited_table(cls):
            return Column(ForeignKey('MenuItem.itemId'), primary_key=True)
        else:
            return Column(Integer, primary_key=True)

class MenuItem(Base, dict):
    def __init__(self, itemName, price, discount):
        self.itemName = itemName
        self.price = price
        self.discount = discount

    def __repr__(self):
        return self.itemName + ": " + "${:3,.2f}".format(self.price)

    __tablename__ = 'MenuItem'

    itemId = Column(Integer, primary_key=True)
    itemName = Column(String)
    price = Column(Integer)
    discount = Column(Integer)

    def ApplyDiscount(self,discount):
        if discount > 0:
            amtD = self.price * discount
            self.price = self.price - amtD
        else:
            self.price = self.price

    # @abstractmethod
    # def GetItemType():
    #     pass


class EntreItem(HasIdMixin, MenuItem):
    def __init__(self, entreType, *args, **kwargs):
        self.ENTRE_TYPES = ("Pizza", "Pasta", "Chicken")
        if entreType not in self.ENTRE_TYPES:
            self.entreType = "Pizza"
        else:
            self.entreType = entreType
        self.modifications = []
        super(EntreItem, self).__init__(*args, **kwargs)

    __tablename__ = 'EntreItem'
    eType = Column(String)

    def ModifyEntre(self, mod):
        if mod in self.modifications:
            return
        else:
            self.modifications.append(mod)

    def __repr__(self):
        return  self.entreType + ": " + super().__repr__()

    def GetItemType():
        return "Entre"

class SideItem(HasIdMixin, MenuItem):
    def __init__(self, sideType, *args, **kwargs):
        self.SIDE_MENU = ("Bread Sticks", "Side Salad", "Dipping Sauce")
        if sideType not in self.SIDE_MENU:
            self.sideType = "none"
        else:
            self.sideType = sideType
        super(SideItem, self).__init__(*args, **kwargs)

    __tablename__ = 'SideItem'
    sType = Column(String)
    
    def __repr__(self):
        return self.sideType +": " + super().__repr__() 

    def GetItemType():
        return "Side"


class DessertItem(HasIdMixin, MenuItem, dict):
    def __init__(self, dessertType, *args, **kwargs):
        self.DESSERT_OPTIONS = ("Cake", "Pie", "Churros")
        if dessertType not in self.DESSERT_OPTIONS:
            self.dessertType = "none"
        else:
            self.dessertType = dessertType
        super(DessertItem, self).__init__(*args, **kwargs)

    __tablename__ = 'DessertItem'
    dType = Column(String)

    def sliceCake(self):
        if self.dessertType == "Cake":
            sliced = str(input("Would you like your cake sliced? (y/n) ")).lower().strip()
            while sliced not in ("y","n"):
                sliced = str(input("Would you like your cake sliced? (y/n) ")).lower().strip()
            if sliced == "y":
                self.dessertType = "Sliced Cake"
            else:
                self.dessertType = "Unsliced Cake"

    def __repr__(self):
        return self.dessertType + ": " + super().__repr__()
    
    def GetItemType():
        return "Dessert"

class MenuItemFactory(object):
    @classmethod
    def create(cls, itemType, *args):
        itemType = itemType.lower().strip()

        if itemType == 'entre':
            return EntreItem(*args)
        elif itemType == 'side':
            return SideItem(*args)
        elif itemType == 'dessert':
            return DessertItem(*args)

    