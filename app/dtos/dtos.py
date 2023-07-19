from decimal import Decimal

from pydantic import BaseModel

from app.dtos.invoice import BaseInvoice
from app.dtos.invoice_line import BaseInvoiceLine


class InvoiceLineDTO(BaseInvoiceLine):
    subtotal_line: int
    total_line: Decimal


class InvoiceDTO(BaseInvoice):
    subtotal: int
    total: Decimal
    lines: list[InvoiceLineDTO]


class ResponseDTO(BaseModel):
    invoices: list[InvoiceDTO]
    invoices_count: int
    invoices_total: Decimal
