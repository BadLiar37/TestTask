from pydantic import BaseModel
from decimal import Decimal

from app.dao.invoice_line import InvoiceLineDAO


class BaseInvoice(BaseModel):
    title: str


class InvoiceDAO(BaseInvoice):
    id: int
    discount: Decimal
    invoice_lines: list[InvoiceLineDAO]

    class Config:
        from_attributes = True
