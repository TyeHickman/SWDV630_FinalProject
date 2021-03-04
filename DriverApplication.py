from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import synonym_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from OrderFacade import OrderFacade, OrderItem
from SystemAdministrator import SystemAdministrator
from StoreLocation import StoreLocation

import base



def main():
    print("Application Starting...")
    print("Creating In-memory database...")
    engine = create_engine('sqlite:///:memory:', echo=False)
    base.Base.metadata.create_all(engine)
    print("Database Created...")
    print("Adding System Administrator...")
    SysAdm = SystemAdministrator("admin01", "super@user.com", "123456")
    
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(SysAdm)
    sa = session.query(SystemAdministrator).first()
    print(sa)
    print("Administrator created...")
    print("Starting Store Location Creation Process...")
    store = sa.CreateStoreLocation()
    print("Created this store: ")
    print(store)



main()