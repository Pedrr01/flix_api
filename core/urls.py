from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api_v1/', include('authentication.urls_v1')),
    path('api_v1/', include('genres.urls_v1')),
    path('api_v1/', include('actors.urls_v1')),
    path('api_v1/', include('movies.urls_v1')),
    path('api_v1/', include('reviews.urls_v1')),
]
