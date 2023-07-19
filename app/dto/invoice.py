from decimal import Decimal


from app.dao.invoice import BaseInvoice
from app.dto.invoice_line import InvoiceLineDTO


class InvoiceDTO(BaseInvoice):
    subtotal: int
    total: Decimal
    lines: list[InvoiceLineDTO]
