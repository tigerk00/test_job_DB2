from rest_framework.pagination import PageNumberPagination


class MessagesPagination(PageNumberPagination):
    page_size = 10