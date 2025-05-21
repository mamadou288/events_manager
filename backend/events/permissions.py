from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsEventCreatorOrReadOnly(BasePermission):
    """
    Autorise uniquement le créateur de l'événement à modifier ou supprimer.
    Les autres peuvent juste lire (GET).
    """

    def has_object_permission(self, request, view, obj):
        # Lecture autorisée pour tous les utilisateurs authentifiés
        if request.method in SAFE_METHODS:
            return True
        # Modification ou suppression uniquement par le créateur
        return obj.creator == request.user
