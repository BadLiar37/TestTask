from fastapi import FastAPI
from starlette.requests import Request

from starlette.responses import JSONResponse

from app.core.constants import BASE_PREFIX
from app.core.configuration import engine, Base
from app.core.exceptions.exceptions import PaginationException
from app.routers import invoices

app = FastAPI()


@app.exception_handler(PaginationException)
async def pagination_exception_handler(request: Request, exc: PaginationException) -> JSONResponse:
    """
    Custom handler for PaginationException
    :param request:
    :param exc:
    :return: JSONResponse - exception information
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Exception!: {exc.detail}"},
    )


Base.metadata.create_all(bind=engine)
app.include_router(invoices.router, tags=["Invoices"], prefix=BASE_PREFIX + "invoices")
