from decimal import Decimal

from app.dto.invoice_line import InvoiceLineDTO
from app.dto.invoice_response import InvoiceResponseDTO
from app.models.models import InvoiceLine
from app.dao.invoice import InvoiceDAO
from app.dto.invoice import InvoiceDTO


class InvoiceManager:
    @staticmethod
    async def convert_invoice_model_to_response_dto(
            invoices: list[InvoiceDAO], lte: int, gte: int
    ) -> InvoiceResponseDTO:
        response_invoices: list[InvoiceDTO] = []
        total_list: list[Decimal] = []
        for invoice in invoices:
            response_invoice_lines, subtotal_line_list, total_line_list = (
                await InvoiceManager.convert_invoice_line_dto(
                    invoice.invoice_lines, invoice.discount
                )
            )
            response_invoice = await InvoiceManager.convert_invoice_to_dto(
                invoice, response_invoice_lines,
                subtotal_line_list, total_line_list
            )
            if gte <= response_invoice.total < lte or lte == 0 and gte <= response_invoice.total:
                response_invoices.append(response_invoice)
                total_list.append(response_invoice.total)
        response_invoice_schema = InvoiceResponseDTO(
            invoices=response_invoices,
            invoices_count=len(response_invoices),
            invoices_total=sum(total_list)
        )

        return response_invoice_schema

    @staticmethod
    async def convert_invoice_line_dto(
            invoice_lines: list[InvoiceLine],
            discount: Decimal
    ) -> tuple[list[InvoiceLineDTO], list[int], list[Decimal]]:
        response_invoice_lines: list[InvoiceLineDTO] = []
        subtotal_line_list: list[int] = []
        total_line_list: list[Decimal] = []

        for invoice_line in invoice_lines:
            subtotal_line = invoice_line.quantity * invoice_line.price_per_one
            total_line = subtotal_line * (1 - discount / 100)
            response_invoice_line = InvoiceLineDTO(
                title=invoice_line.title,
                quantity=invoice_line.quantity,
                price_per_one=invoice_line.price_per_one,
                subtotal_line=subtotal_line,
                total_line=total_line
            )
            response_invoice_lines.append(response_invoice_line)
            subtotal_line_list.append(subtotal_line)
            total_line_list.append(total_line)

        return response_invoice_lines, subtotal_line_list, total_line_list

    @staticmethod
    async def convert_invoice_to_dto(
            invoice: InvoiceDAO,
            response_invoice_lines: list[InvoiceLineDTO],
            subtotal_line_list: list[int],
            total_line_list: list[Decimal]
    ) -> InvoiceDTO:
        response_invoice = InvoiceDTO(
            title=invoice.title,
            subtotal=sum(subtotal_line_list),
            total=sum(total_line_list),
            lines=response_invoice_lines
        )
        return response_invoice
