from OrderTicket import OrderTicket
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative.api import synonym_for
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from SystemAdministrator import SystemAdministrator
from StoreLocation import StoreLocation
from UserProfile import UserProfile
from MemberUser import MemberUser

import base



def main():
    print("Application Starting...")
    print("Creating In-memory database...")
    engine = create_engine('sqlite:///:memory:', echo=False)
    base.Base.metadata.create_all(engine)
    print("Database Created...")
    print("Adding System Administrator...")
    SysAdm = SystemAdministrator("admin01", "super@user.com", "123456")
    
    Session = sessionmaker(bind=engine, autocommit=True)
    session = Session()

    session.add(SysAdm)
    sa = session.query(SystemAdministrator).first()
    print(sa)
    print("Administrator created...")
    print("Starting Store Location Creation Process...")
    # store = sa.CreateStoreLocation()
    # Got tired of typing this so I created a test method...
    store = sa.CreateTestLocation()
    print("Created this store: ")
    print(store)
    session.add(store)
    s1 = session.query(StoreLocation).first()


    print("\nCreating Test User...")
    testUser = UserProfile("test@user.com", "1 Test Road")
    session.add(testUser)
    tUser = session.query(UserProfile).first()
    print(tUser)

    print("\nCreating Test User as a Member User")
    testMember = MemberUser(tUser, 'testMember', '123456')
    session.add(testMember)
    tMember = session.query(MemberUser).first()
    print(tMember)

    print("\nTesting Order process...")
    # testOrder = s1.createOrder()
    # Created a test order for this one as well.
    testOrder = s1.createTestOrder(tMember.userInfo.userId)
    session.add(testOrder)
    tOrder = session.query(OrderTicket).first()
    print(tOrder)


main()