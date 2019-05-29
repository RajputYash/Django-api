from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class UserLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10

class UsrPageNumberPagination(PageNumberPagination):
    page_size = 1