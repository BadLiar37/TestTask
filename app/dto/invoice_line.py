from decimal import Decimal

from app.dao.invoice_line import BaseInvoiceLine


class InvoiceLineDTO(BaseInvoiceLine):
    subtotal_line: int
    total_line: Decimal
