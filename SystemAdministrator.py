# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from StoreLocation import StoreLocation
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
        sMenu = ['Pizza', 'Chicken', 'Cake']
        
        newLocation = StoreLocation(sName, sCode, sAddress, sMenu, createdBy)
        return newLocation
    # TODO: create menu item method
    # TODO: modify store location menu