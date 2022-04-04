from rest_framework.permissions import BasePermission


class IsGuest(BasePermission):
    def has_object_permission(self, request, view, reservation):
        return reservation.guest == request.user


class IsRoomOwner(BasePermission):
    def has_object_permission(self, request, view, reservation):
        return reservation.room.host == request.user
