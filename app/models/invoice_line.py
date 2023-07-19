from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey

from app.core.configuration import Base


class InvoiceLine(Base):
    """
    InvoiceLine model in database
    """
    __tablename__ = "invoice_lines"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    quantity = Column(Integer)
    price_per_one = Column(DECIMAL(precision=10, scale=2))
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
