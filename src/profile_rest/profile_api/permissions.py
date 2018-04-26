from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    only user can edit his own
    """

    def has_object_permission(self, request, view, obj):
        # Get같이 non-editable 한 approach
        if request.method in permissions.SAFE_METHODS:
            return True
        # if user's id is same as object's id
        return obj.id == request.user.id
