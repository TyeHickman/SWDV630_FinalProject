from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class UserProfile(Base):
    def __init__(self, emailAddress, deliveryAddress):
        self.userId = None
        self.emailAddress = emailAddress
        self.delivery = deliveryAddress

    __tablename__ = 'UserProfile'
    userId = Column(Integer, primary_key=True)
    email = Column(String)
    delAddress = Column(String)
    child = relationship("MemberUser", uselist=False, back_populates="parent")

    def __repr__(self):
        return "UserId: {0}\nEmail: {1}\nAddress: {2}".format(self.userId, self.emailAddress, self.delivery)
