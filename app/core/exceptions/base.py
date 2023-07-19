from starlette.exceptions import HTTPException


class BaseHttpException(HTTPException):
    """
    Base exception for all custom exceptions
    """
    status_code: int = 400
    detail: str = "None"

    def __init__(self):
        super().__init__(
            status_code=self.status_code, detail=self.detail
        )
