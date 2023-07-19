from app.core.exceptions.base import BaseHttpException


class PaginationException(BaseHttpException):
    """
    Exception raises when limit or skip request query params are incorrect
    """
    status_code = 406
    detail = "Invalid skip or limit value"


class NoContentException(BaseHttpException):
    """
    Exception raises when nothing is found in the database
    """
    status_code = 204
    detail = "Nothing found with such criteria"
