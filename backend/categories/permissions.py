from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Admin users can perform all operations.
    Sales Managers and Customers can only view data.
    """

    def has_permission(self, request, view):

        # Allow GET, HEAD, OPTIONS for authenticated users
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        # Allow write operations only for ADMIN role
        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )