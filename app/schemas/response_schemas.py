from decimal import Decimal

from pydantic import BaseModel

from app.schemas.invoice import BaseInvoice
from app.schemas.invoice_line import BaseInvoiceLine


class ResponseInvoiceLine(BaseInvoiceLine):
    subtotal_line: int
    total_line: Decimal


class ResponseInvoice(BaseInvoice):
    subtotal: int
    total: Decimal
    lines: list[ResponseInvoiceLine]


class ResponseInvoiceSchema(BaseModel):
    invoices: list[ResponseInvoice]
    invoices_count: int
    invoices_total: Decimal
