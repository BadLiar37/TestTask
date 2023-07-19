from decimal import Decimal

from pydantic import BaseModel

from app.dto.invoice import InvoiceDTO


class ResponseDTO(BaseModel):
    invoices: list[InvoiceDTO]
    invoices_count: int
    invoices_total: Decimal
