from decimal import Decimal

from pydantic import BaseModel

from app.dto.invoice import InvoiceDTO


class InvoiceResponseDTO(BaseModel):
    """
    InvoiceDTO for sending responses
    """
    invoices: list[InvoiceDTO]
    invoices_count: int
    invoices_total: Decimal
