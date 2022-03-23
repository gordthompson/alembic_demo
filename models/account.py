from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .__base import Base


class Account(Base):
    __tablename__ = "account"
    account_number = Column(Integer, primary_key=True)
    customer_name = Column(String(50))
    invoices = relationship("Invoice", back_populates="account")
