from rest_framework import viewsets
from movies.serializers import PersonSerializer, MovieSerializer

from movies.models import Movie, Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
