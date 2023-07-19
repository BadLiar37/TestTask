from decimal import Decimal

from pydantic import BaseModel


class BaseInvoiceLine(BaseModel):
    title: str
    quantity: int
    price_per_one: Decimal


class InvoiceLine(BaseInvoiceLine):
    id: int

    class Config:
        from_attributes = True
