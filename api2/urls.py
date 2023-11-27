from django.urls import path

from .views import PersonAPI, ProfileAPI

urlpatterns = [
    path('api/person', PersonAPI.as_view()),
    path('api/profile', ProfileAPI.as_view()),


]