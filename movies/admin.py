from django.contrib import admin

from .models import Person, Movie


class CastingInline(admin.TabularInline):
    model = Movie.casting.through
    verbose_name = "Casting"
    verbose_name_plural = "Casting"


class DirectorsInline(admin.TabularInline):
    model = Movie.directors.through
    verbose_name = "Director"
    verbose_name_plural = "Director"


class ProducerInline(admin.TabularInline):
    model = Movie.producers.through
    verbose_name = "Producer"
    verbose_name_plural = "Producers"


class MovieAdmin(admin.ModelAdmin):
    """Person admin."""
    model = Movie
    inlines = [
        CastingInline,
        DirectorsInline,
        ProducerInline,
    ]
    exclude = (
        'casting',
        'directors',
        'producers',
    )


admin.site.register(Movie, MovieAdmin)


class MoviesAsActorInline(admin.TabularInline):
    model = Movie.casting.through
    verbose_name = "Movie As Actor"
    verbose_name_plural = "Movies As Actor"


class MoviesAsDirectorsInline(admin.TabularInline):
    model = Movie.directors.through
    verbose_name = "Movie As Director"
    verbose_name_plural = "Movies As Director"


class MoviesAsProducerInline(admin.TabularInline):
    model = Movie.producers.through
    verbose_name = "Movie As Producer"
    verbose_name_plural = "Movies As Producer"


class PersonAdmin(admin.ModelAdmin):
    """Person admin."""
    model = Person
    inlines = [
        MoviesAsActorInline,
        MoviesAsDirectorsInline,
        MoviesAsProducerInline,
    ]


admin.site.register(Person, PersonAdmin)
