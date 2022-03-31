from rest_framework.permissions import BasePermission


class IsUserRoom(BasePermission):
    def has_object_permission(self, request, view, room):
        return room.host == request.user
