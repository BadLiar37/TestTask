from app.repository.base import BaseRepository
from app.models.models import Invoice


class InvoiceRepository(BaseRepository[Invoice]):
    def __init__(self, model: Invoice):
        super().__init__(model)
