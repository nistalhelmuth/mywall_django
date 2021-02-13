from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

DEFAULT_PAGE = 50
DEFAULT_PAGE_LIMIT = 50

class CustomPagination(LimitOffsetPagination):
    default_limit = DEFAULT_PAGE
    max_limit = DEFAULT_PAGE_LIMIT