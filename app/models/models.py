from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from app.core.configuration import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    discount = Column(DECIMAL(precision=10, scale=2))

    invoice_lines = relationship("InvoiceLine", backref="invoice")


class InvoiceLine(Base):
    __tablename__ = "invoice_lines"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    quantity = Column(Integer)
    price_per_one = Column(DECIMAL(precision=10, scale=2))
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
