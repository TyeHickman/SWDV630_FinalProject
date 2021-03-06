# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import PickleType
from StoreLocation import StoreLocation
from MenuItemFactory import MenuItemFactory
from base import Base

class SystemAdministrator(Base):

    def __init__(self, userName, email, password):
        self.userName = userName
        self.email = email
        self.password = password
    
    __tablename__ = 'SystemAdministrator'

    admID = Column(Integer, primary_key=True)
    userName = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return "UserName: {0} \nEmail: {1}".format(self.userName, self.email)

    def CreateStoreLocation(self):
        createdBy = self.email
        sName = input(str("Store Name? "))
        sCode = input(str("Store Code? (hint: store001) "))
        sAddress = input(str("Store Address? "))
        sMenu = self.generateStandardMenu()
        
        newLocation = StoreLocation(sName, sCode, sAddress, sMenu, createdBy)
        return newLocation
    # TODO: create menu item method
    # TODO: modify store location menu

    def generateStandardMenu(self):
        # pizza:
            # Pepperoni
            # Cheese
        # pasta
            # Alfredo
        # chicken
            # BBQ
        pizza1 = MenuItemFactory.create('entre','Pizza','Pepperoni', 15, 0)
        pizza2 = MenuItemFactory.create('entre', 'Pizza', 'Cheese', 10, 0)
        pasta1 = MenuItemFactory.create('entre', 'Pasta', 'Alfredo', 10, 0)
        chicken1 = MenuItemFactory.create('entre', 'Chicken', 'BBQ', 8, 0)
        menuEntres = [pizza1,pizza2,pasta1, chicken1]
        # bread sticks
        # side salad
        # dipping sauce
        bSticks = MenuItemFactory.create('side', 'Bread Sticks', 'Bread Sticks', 5, 0)
        sSalad = MenuItemFactory.create('side', 'Side Salad', 'Side Salad', 5, 0)
        dSauce = MenuItemFactory.create('side', 'Dipping Sauce', 'Dipping Sauce', 5, 0)
        menuSides = [bSticks, sSalad, dSauce]
        # Cake
        # Pie
        # Churros
        dCake = MenuItemFactory.create('dessert', 'Cake', 'Chocolate Cake', 6, 0)
        dPie = MenuItemFactory.create('dessert', 'Pie', 'Apple Pie', 6, 0)
        dChurros = MenuItemFactory.create('dessert', 'Churros', 'Churros', 6, 0)
        menuDesserts = [dCake, dPie, dChurros]
        menuDict = {
            'Entres': menuEntres,
            'Sides': menuSides,
            'Desserts': menuDesserts
        }
        return menuDict