from django.urls import path

from .views import PersonAPI, ProfileAPI, StoreAPI, ProductAPI

urlpatterns = [
    path('api/person', PersonAPI.as_view()),
    path('api/profile', ProfileAPI.as_view()),
    path('api/store', StoreAPI.as_view()),
    path('api/product', ProductAPI.as_view()),
]