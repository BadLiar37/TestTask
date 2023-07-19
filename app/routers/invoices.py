from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.converter import Converter
from app.exceptions.exceptions import NoContentException
from app.core.helpers import common_parameters, get_db, filter_params
from app.models.models import Invoice
from app.schemas.response_schemas import ResponseInvoiceSchema
from app.repository.invoice_repository import InvoiceRepository

router = APIRouter()
repository = InvoiceRepository(Invoice)


@router.get("/")
async def get_invoices(
    db: Session = Depends(get_db),
    params: dict = Depends(common_parameters),
    filters: dict = Depends(filter_params)
) -> ResponseInvoiceSchema:
    invoices = await repository.get_items(db, **params)
    if not invoices:
        raise NoContentException
    result = await Converter.convert_invoice_model_to_response_schema(invoices, **filters)

    return result
