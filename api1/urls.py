from django.urls import path
from .views import BookAPIView, AuthorAPIView, LanguageAPIView, ApiOverview, add_piple, view_piple, update_piple, \
    delete_piple, ViewBook

urlpatterns = [
    path('', ApiOverview, name='home' ),
    path('create/', add_piple, name='add-piple'),
    path('all/', view_piple, name='view-piple'),
    path('update/<int:pk>/', update_piple, name='update_piple'),
    path('piple/<int:pk>/delete', delete_piple, name='delete_piple'),


    path('book/create', BookAPIView.as_view()),
    # path('api/book', BookAPIView.as_view()),
    path('api/author', AuthorAPIView.as_view()),
    path('api/lang', LanguageAPIView.as_view()),
    path('allbook', ViewBook.as_view()),

]
