from fastapi import FastAPI

from app.core.constants import BASE_PREFIX
from app.core.configuration import engine
from app.models import models
from app.routers import invoices
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(invoices.router, tags=["Invoices"], prefix=BASE_PREFIX + "invoices")
