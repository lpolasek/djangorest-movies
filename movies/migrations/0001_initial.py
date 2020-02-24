# Generated by Django 3.0.3 on 2020-02-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'last_name',
                    models.CharField(max_length=50)
                ),
                (
                    'first_name',
                    models.CharField(max_length=50)
                ),
                (
                    'aliases',
                    models.CharField(
                        blank=True,
                        max_length=500
                    )
                ),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'name',
                    models.CharField(max_length=50)
                ),
                (
                    'release_year',
                    models.PositiveSmallIntegerField()
                ),
                (
                    'casting',
                    models.ManyToManyField(
                        blank=True,
                        related_name='movies_as_actor',
                        to='movies.Person'
                    )
                ),
                (
                    'directors',
                    models.ManyToManyField(
                        blank=True,
                        related_name='movies_as_director',
                        to='movies.Person'
                    )
                ),
                (
                    'producers',
                    models.ManyToManyField(
                        blank=True,
                        related_name='movies_as_producer',
                        to='movies.Person'
                    )
                ),
            ],
        ),
    ]
