from app.core.configuration import SessionLocal


def get_db() -> None:
    """
    Generator for database session
    :return: None
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def common_parameters(skip: int = 0, limit: int = 100) -> dict[str, int]:
    """
    Dependency for query params
    :param skip:
    :param limit:
    :return: dict[str,int] - params for sql query
    """
    return {"skip": skip, "limit": limit}


async def filter_params(lte: int = 0, gte: int = 0) -> dict[str, int]:
    """
    Dependency for filtering invoices
    :param gte:
    :param lte:
    :return: dict[str,int] - params for filtering invoices
    """
    return {"lte": lte, "gte": gte}
