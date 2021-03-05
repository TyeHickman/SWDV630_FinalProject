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

class MenuItem(Base, metaclass = ABCMeta):
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

    @abstractmethod
    def GetItemType():
        pass


class EntreItem(HasIdMixin, MenuItem):
    def __init__(self, entreType, size, *args, **kwargs):
        self.ENTRE_TYPES = ("Pizza", "Pasta", "Chicken")
        self.SIZES = ("Small", "Medium", "Large", "Chicago")
        if entreType not in self.ENTRE_TYPES:
            self.entreType = "Pizza"
        else:
            self.entreType = entreType
        if size not in self.SIZES:
            self.size = "Small"
        else:
            self.size = size
        self.modifications = []
        super(EntreItem, self).__init__(*args, **kwargs)

    __tablename__ = 'EntreItem'
    eType = Column(String)
    eSize = Column(String)

    def ModifyEntre(self, mod):
        if mod in self.modifications:
            return
        else:
            self.modifications.append(mod)

    def UpSize(self):
        os = self.SIZES.index(self.size)
        self.size = self.SIZES[os + 1]

    def __repr__(self):
        return  self.size + " " + self.entreType + ": " + super().__repr__()

    def GetItemType():
        return "Entre"

class SideItem(HasIdMixin, MenuItem):
    def __init__(self, sideType, sideQuantity, *args, **kwargs):
        self.SIDE_MENU = ("Bread", "Side Salad", "Dipping Sauce")
        if sideType not in self.SIDE_MENU:
            self.sideType = "none"
        else:
            self.sideType = sideType
        
        if self.sideType == "none":
            self.sideQuantity = 0
        else:
            self.sideQuantity = sideQuantity
        super(SideItem, self).__init__(*args, **kwargs)

    __tablename__ = 'SideItem'
    sType = Column(String)
    sQuantity = Column(Integer)

    def doubleOrder(self):
        self.sideQuantity = self.sideQuantity *2
    
    def chooseSalad(self):
        SALADS = ("ceasar", "cobb")
        if self.sideType == "Side Salad" or self.sideType == self.SIDE_MENU[1]:
            choice = str(input("Choose Salad Type: Ceasar, Cobb: ")).lower().strip()
            while choice not in SALADS:
                print("Selection Unavailable, Please try again.")
                choice = str(input("Choose Salad Type: Ceasar, Cobb: ")).lower().strip()
            self.sideType = choice
    def __repr__(self):
        return self.sideType +": " + super().__repr__() 

    def GetItemType():
        return "Side"


class DessertItem(HasIdMixin, MenuItem):
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