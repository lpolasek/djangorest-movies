from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    # TODO: convert to string list
    aliases = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    release_year = models.PositiveSmallIntegerField()

    casting = models.ManyToManyField(Person,
                                     blank=True,
                                     related_name='movies_as_actor')
    directors = models.ManyToManyField(Person,
                                       blank=True,
                                       related_name='movies_as_director')
    producers = models.ManyToManyField(Person, blank=True,
                                       related_name='movies_as_producer')

    def __str__(self):
        return '%s (%d)' % (self.name, self.release_year)
