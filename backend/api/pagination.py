from rest_framework.pagination import PageNumberPagination


class PaginacaoCustomizada(PageNumberPagination):
    page_size = 5