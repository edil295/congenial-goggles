from django.shortcuts import render
from .models import Category, Firm, Item
from .serializers import CategorySerializer, FirmSerializer, ItemSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, \
    DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FirmGenericsViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin,
                          DestroyModelMixin, RetrieveModelMixin):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class ItemModelViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

