from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dto.invoice_response import InvoiceResponseDTO
from app.services.invoice_manager import InvoiceManager
from app.exceptions.exceptions import NoContentException
from app.core.helpers import common_parameters, get_db, filter_params
from app.models.models import Invoice
from app.repository.invoice_repository import InvoiceRepository

router = APIRouter()
repository = InvoiceRepository(Invoice)


@router.get("/")
async def get_invoices(
    db: Session = Depends(get_db),
    params: dict = Depends(common_parameters),
    filters: dict = Depends(filter_params)
) -> InvoiceResponseDTO:
    invoices = await repository.get_items(db, **params)
    if not invoices:
        raise NoContentException
    result = await InvoiceManager.convert_invoice_model_to_response_dto(invoices, **filters)

    return result
