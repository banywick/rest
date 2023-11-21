from django.urls import path
from .views import BookAPIView, AuthorAPIView, data_create_view

urlpatterns = [
    path('api/book', BookAPIView.as_view()),
    path('api/author', AuthorAPIView.as_view()),
    path('api/data/', data_create_view, name='data-create')


]
# {"name":"man"}