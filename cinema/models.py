from django.db import models
# Create your models here.

class Genre(models.Model):
	genre_id = models.AutoField(primary_key=True)
	genre_name = models.CharField(max_length=20)

	def __str__(self):
		return self.genre_name

class Movie(models.Model):
	movie_id = models.AutoField(primary_key=True)
	movie_name = models.CharField(max_length=60)
	age = models.SmallIntegerField(default=0)
	genre = models.ForeignKey(Genre)

	#table의 각 tuple을 대표하는 값을 나타낸다.
	def __str__(self):
		return self.move_name

class Cinema_brand(models.Model):
	cinema_brand_id = models.AutoField(primary_key=True)
	cinema_brand_name = models.CharField(max_length=30)

	def __str__(self):
		return self.cinema_brand_name

class Cinema_branch(models.Model):
	cinema_branch_id = models.AutoField(primary_key=True)
	brand = models.ForeignKey(Cinema_brand)
	cinema_branch_name = models.CharField(max_length=40)
	lat = models.FloatField(default=0)
	lng = models.FloatField(default=0)
