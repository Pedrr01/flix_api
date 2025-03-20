from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializers

class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers





