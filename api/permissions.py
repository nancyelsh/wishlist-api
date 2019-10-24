from rest_framework.permissions import BasePermission
from .serializers import ItemListSerializer, ItemDetailsSerializer, UserSerializer

class IsStaffOrUser(BasePermission):
	message = "You don't have access."

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (request.user == obj.user):
			return True
		return False