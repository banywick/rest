from django.urls import path
from .views import BookAPIView,AuthorAPIView

urlpatterns = [
    path('api/book', BookAPIView.as_view()),
    path('api/author', AuthorAPIView.as_view())

]
