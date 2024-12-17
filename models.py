from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,declarative_base

Base = declarative_base()

class LAB(Base):
    __tablename__ = "labs"
    id = Column(Integer,primary_key= True)
    name = Column(String,nullable=False)
    section = Column(String,unique=True,nullable=False)

    tests = relationship("Test",back_populates="lab")

    def __repr__(self):
        return f"LAB(id = {self.id}, name= '{self.name}', section = '{self.section}')"
    

class Test(Base):
    __tablename__="tests"
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    lab_id = Column(Integer,ForeignKey("labs.id"))

    lab = relationship("LAB",back_populates="tests")  

    def __repr__(self):
        return f"Test(id= {self.id}, name = '{self.name}',price = {self.price}, lab_id = {self.lab_id})"