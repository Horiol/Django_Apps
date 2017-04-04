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

class Album(models.Model):
    albumid = models.IntegerField(db_column='AlbumId', primary_key=True)
    title = models.TextField(db_column='title')
    artistid = models.ForeignKey(Artist, on_delete=models.CASCADE, db_column="ArtistId")

class Genre(models.Model):
    genreid = models.IntegerField(db_column='GenreId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.


class Playlist(models.Model):
    playlistid = models.IntegerField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

class Track(models.Model):
    trackid = models.IntegerField(db_column='TrackId', primary_key=True)
    name = models.TextField(db_column='Name')
    genreid = models.ForeignKey(Genre, db_column="GenreId")
    albumid = models.ForeignKey(Album, db_column="AlbumId")
    miliseconds = models.IntegerField(db_column="Milliseconds")
