from rest_framework import serializers
from django.contrib.auth.models import User

from items.models import Item, FavoriteItem


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "item-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )

	added_by = UserSerializer()
	likes = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['id', 'image', 'name', 'description', 'detail', 'added_by', 'likes']

	def get_likes(self, obj):
		likes = len(obj.favoriteitem_set.all().values_list('user'))
		# past_bookings = BookingSerializer(booking_objects, many=True)
		return likes

class ItemDetailsSerializer(serializers.ModelSerializer):
	likes_list = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'likes_list']

	def get_likes_list(self, obj):
		liked_by = obj.favoriteitem_set.all().values_list('user')
		# users = liked_by.filter(id=liked_by)
		# likes_list = ItemListSerializer(liked_by, many=True)
		return liked_by
		# return users