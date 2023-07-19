from typing import Dict, Any

from starlette.exceptions import HTTPException


class BaseHttpException(HTTPException):
    status_code: int = 400
    detail: str = "None"

    def __init__(self):
        super().__init__(
            status_code=self.status_code, detail=self.detail
        )
