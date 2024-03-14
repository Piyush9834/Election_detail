from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

    def get_limit(self, request):
        try:
            limit = int(request.query_params.get('limit', self.default_limit))
            if limit < 0:
                raise ValueError("Limit must be a positive integer")
            return min(limit, self.max_limit)
        except (TypeError, ValueError):
            return self.default_limit
