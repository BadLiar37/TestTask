from pydantic import BaseModel
from decimal import Decimal

from app.dtos.invoice_line import InvoiceLine


class BaseInvoice(BaseModel):
    title: str


class Invoice(BaseInvoice):
    id: int
    discount: Decimal
    invoice_lines: list[InvoiceLine]

    class Config:
        from_attributes = True
