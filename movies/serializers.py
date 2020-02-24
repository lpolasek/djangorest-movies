from rest_framework import serializers

from movies.models import Movie, Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            'url',
            'last_name',
            'first_name',
            'aliases',
            'movies_as_actor',
            'movies_as_director',
            'movies_as_producer',
        ]


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    roman_release_year = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = [
            'url',
            'name',
            'release_year',
            'roman_release_year',
            'casting',
            'directors',
            'producers',
        ]
