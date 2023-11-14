from django.urls import path
from .views import get_page, get_page2, BookAPIView

urlpatterns = [
    path('', get_page, name='page'),
    path('api2/', get_page2, name='page2'),
    path('api/new', BookAPIView.as_view(), name='apinew')

]
