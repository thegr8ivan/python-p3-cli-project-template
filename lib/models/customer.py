from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    orders = relationship("Order", back_populates="customer")

    @classmethod
    def create(cls, session, name, phone):
        customer = cls(name=name, phone=phone)
        session.add(customer)
        session.commit()
        return customer

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
