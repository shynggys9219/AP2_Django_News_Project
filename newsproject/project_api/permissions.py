from rest_framework import permissions

# Custom permission to check whether user belongs to staff or not
# if not then only Get, Head and OPTIONS will be available
# if yes, then CRUD operations are possible 
class IsStaffOrNot(permissions.BasePermission):

    def has_permission(self, request, view):
        # safe methods are: GET, HEAD and some OPTIONS
        if request.method in permissions.SAFE_METHODS: return True

        return request.user.is_staff
