from app.exceptions.base import BaseHttpException


class PaginationException(BaseHttpException):
    status_code = 406
    detail = "Invalid skip or limit value"


class NoContentException(BaseHttpException):
    status_code = 204
    detail = "Nothing found with such criteria"
