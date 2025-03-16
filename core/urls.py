from django.contrib import admin
from django.urls import path
from genres.views import GenreCretaeListView, GenreRetrivieIpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCretaeListView.as_view(), name='genre-create-list-view'),
    path('genres/<int:pk>/',GenreRetrivieIpdateDestroyView.as_view() ,name='genre-detail-view'),
]
