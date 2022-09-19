from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from my_app import views

router = DefaultRouter()
router.register('item', views.ItemModelViewSet, basename='item')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/list/', views.CategoryListAPIView.as_view()),
    path('category/create/', views.CategoryCreateAPIView.as_view()),
    path('category/update/<int:pk>/', views.CategoryUpdateAPIView.as_view()),
    path('category/delete/<int:pk>/', views.CategoryDestroyAPIView.as_view()),
    path('category/retrieve/<int:pk>/', views.CategoryRetrieveAPIView.as_view()),
    path('firm/', views.FirmGenericsViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('firm/<int:pk>/', views.FirmGenericsViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    path('', include(router.urls))

]

