from django.urls import path
from .views import BookAPIView, AuthorAPIView, LanguageAPIView

urlpatterns = [
    path('api/book', BookAPIView.as_view()),
    path('api/author', AuthorAPIView.as_view()),
    path('api/lang', LanguageAPIView.as_view())

]
