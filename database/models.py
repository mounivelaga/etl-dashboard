from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    amount = Column(Integer, nullable=False)
    order_date = Column(String(20), nullable=False)
