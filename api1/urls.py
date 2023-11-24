from django.urls import path
from .views import ApiOverview, add_piple, view_piple, delete_piple, update_piple

urlpatterns = [
    path('', ApiOverview, name='home' ),
    path('create/', add_piple, name='add-piple'),
    path('all/', view_piple, name='view-piple'),
    path('update/<int:pk>/', update_piple, name='update_piple'),
    path('piple/<int:pk>/delete', delete_piple, name='delete_piple'),




]
