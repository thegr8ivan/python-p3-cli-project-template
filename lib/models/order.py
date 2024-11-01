from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    coffee_type = Column(String, nullable=False)
    size = Column(String, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship("Customer", back_populates="orders")

    @classmethod
    def create(cls, session, coffee_type, size, customer_id):
        order = cls(coffee_type=coffee_type, size=size, customer_id=customer_id)
        session.add(order)
        session.commit()
        return order

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()
