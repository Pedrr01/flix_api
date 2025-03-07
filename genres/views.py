from django.shortcuts import render
from genres.models import Genre
from django.http import JsonResponse

def genre_list_view(request):
    genres = Genre.objects.all()
    data = [{'id' : genre.id, 'name': genre.name} for genre in genres]
    return JsonResponse(data, safe=False)