# Generated by Django 3.0.6 on 2020-05-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200526_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movieid', models.BigIntegerField(db_column='movieId', primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('genres', models.TextField(blank=True, null=True)),
                ('imdbid', models.TextField(blank=True, db_column='imdbId', null=True)),
            ],
            options={
                'db_table': 'movies',
                'managed': False,
            },
        ),
    ]
