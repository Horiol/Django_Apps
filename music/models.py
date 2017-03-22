# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Artist(models.Model):
    artistid = models.IntegerField(db_column='ArtistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Artist'

class Album(models.Model):
    albumid = models.IntegerField(db_column='AlbumId', primary_key=True)
    title = models.TextField(db_column='title')
    artistid = models.ForeignKey(Artist, on_delete=models.CASCADE, db_column="ArtistId")

    class Meta:
        managed = False
        db_table = 'Album'

# Unable to inspect table 'Customer'
# The error was: 'NoneType' object has no attribute 'groups'
class Customer(models.Model):
    customerid=models.IntegerField(db_column='CustomerId', primary_key=True)

# Unable to inspect table 'Employee'
# The error was: 'NoneType' object has no attribute 'groups'


class Genre(models.Model):
    genreid = models.IntegerField(db_column='GenreId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Genre'
# Unable to inspect table 'Invoice'
# The error was: 'NoneType' object has no attribute 'groups'
# Unable to inspect table 'InvoiceLine'
# The error was: 'NoneType' object has no attribute 'groups'


class Mediatype(models.Model):
    mediatypeid = models.IntegerField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MediaType'


class Playlist(models.Model):
    playlistid = models.IntegerField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Playlist'
# Unable to inspect table 'PlaylistTrack'
# The error was: 'NoneType' object has no attribute 'groups'

class Track(models.Model):
    trackid = models.IntegerField(db_column='TrackId', primary_key=True)
    name = models.TextField(db_column='Name')
    genreid = models.ForeignKey(Genre, db_column="GenreId")
    albumid = models.ForeignKey(Album, db_column="AlbumId")
    miliseconds = models.IntegerField(db_column="Milliseconds")

    class Meta:
        db_table = 'Track'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
