from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsStaffOrUser
from items.models import Item, FavoriteItem
from .serializers import ItemListSerializer, ItemDetailsSerializer, UserSerializer

# Create your views here.

class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	# search_fields = ['']
	permission_classes = [AllowAny]

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailsSerializer
	permission_classes = [IsAuthenticated, IsStaffOrUser]
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'