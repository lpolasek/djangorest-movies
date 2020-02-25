from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    aliases = models.CharField(
        max_length=500,
        blank=True,
        help_text='This field is converted to a list using ' +
                  '| as a separator'
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    name = models.CharField(max_length=50)
    release_year = models.PositiveSmallIntegerField()

    @property
    def roman_release_year(self):
        num_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        roman = ''
        num = 0 if self.release_year is None else self.release_year

        while num > 0:
            for i, r in num_map:
                while num >= i:
                    roman += r
                    num -= i

        return roman

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
