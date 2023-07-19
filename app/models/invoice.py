from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship

from app.core.configuration import Base


class Invoice(Base):
    """
    Invoice model in database
    """
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    discount = Column(DECIMAL(precision=10, scale=2))

    invoice_lines = relationship("InvoiceLine", backref="invoice")
