from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.GenreCretaeListView.as_view(), name='genre-create-list-view'),
    path('genres/<int:pk>/', views.GenreRetrivieIpdateDestroyView.as_view() ,name='genre-detail-view'),
]