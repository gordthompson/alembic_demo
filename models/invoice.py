from sqlalchemy import Column, Integer, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship

from .__base import Base


class Invoice(Base):
    __tablename__ = "invoice"
    invoice_number = Column(Integer, primary_key=True)
    account_number = Column(Integer, ForeignKey("account.account_number"), index=True)
    invoice_date = Column(Date)
    invoice_amount = Column(Numeric(18, 4))
    account = relationship("Account", back_populates="invoices")
