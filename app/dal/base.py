from typing import TypeVar, Generic

from sqlalchemy.orm import Session

from app.core.exceptions.exceptions import PaginationException

T = TypeVar("T")


class BaseDAL(Generic[T]):

    def __init__(self, model: T):
        self.model = model

    async def get_items(self,  db: Session, skip: int = 0, limit: int = 100) -> list[T]:
        """
        Get items from database
        :param db:
        :param skip:
        :param limit:
        :return: list[T] - result set
        """
        if limit < 1:
            raise PaginationException
        return db.query(self.model).offset(skip).limit(limit).all()
