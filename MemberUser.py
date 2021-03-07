from sqlalchemy import Column, Integer, String, PickleType, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class MemberUser(Base):
    def __init__(self, userInfo, userName, password, easyOrder=None, rewards=0):
        self.memberId = None
        self.userInfo = userInfo
        self.userName = userName
        self.password = password
        self.easyOrder = easyOrder
        self.memberRewards = rewards

    __tablename__ = 'MemberUser'
    memberId = Column(Integer, primary_key=True)
    userProfile = Column(PickleType)
    userName = Column(String)
    password = Column(String)
    easyOrder = Column(PickleType)
    parent_id = Column(Integer, ForeignKey('UserProfile.userId'))
    parent = relationship("UserProfile", back_populates="child")

    def __repr__(self):
        return "\nUserName: {0}\nReward Points: {1}\n{2}".format(self.userName, self.memberRewards, self.userInfo)