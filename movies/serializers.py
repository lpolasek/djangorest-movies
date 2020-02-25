from django.db import models
from rest_framework import serializers

from movies.models import Movie, Person


class TokenizedListField(serializers.ListField):
    """
    Saves a list of serializers as a token separated string.
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', '|')
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        """
        List of dicts of native values <- List of dicts of primitive datatypes.
        """
        if html.is_html_input(data):
            data = html.parse_html_list(data, default=[])

        if not isinstance(data, list):
            message = self.error_messages['not_a_list'].format(
                input_type=type(data).__name__
            )
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='not_a_list')

        if not self.allow_empty and len(data) == 0:
            message = self.error_messages['empty']
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='empty')

        ret = []
        errors = []

        for item in data:
            try:
                validated = self.child.run_validation(item)
            except ValidationError as exc:
                errors.append(exc.detail)
            else:
                ret.append(validated)
                errors.append({})

        if any(errors):
            raise ValidationError(errors)

        return self.token.join(ret)

    def to_representation(self, data):
        """
        List of object instances -> List of dicts of primitive datatypes.
        """
        # Dealing with nested relationships, data can be a Manager,
        # so, first get a queryset from the Manager if needed
        iterable = data.all() if isinstance(data, models.Manager) else data

        return [
            self.child.to_representation(item)
            for item in iterable.split(self.token)
        ]


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    aliases = TokenizedListField(child=serializers.CharField())

    class Meta:
        model = Person
        fields = [
            'id',
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
            'id',
            'url',
            'name',
            'release_year',
            'roman_release_year',
            'casting',
            'directors',
            'producers',
        ]
