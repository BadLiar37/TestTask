from app.core.configuration import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def common_parameters(skip: int = 0, limit: int = 100) -> dict[str, int]:
    return {"skip": skip, "limit": limit}


async def filter_params(lte: int = 0, gte: int = 0) -> dict[str, int]:
    return {"lte": lte, "gte": gte}
