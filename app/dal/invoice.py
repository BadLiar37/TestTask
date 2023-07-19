from app.dal.base import BaseDAL
from app.models.invoice import Invoice


class InvoiceDAL(BaseDAL[Invoice]):
    def __init__(self, model: Invoice):
        super().__init__(model)
