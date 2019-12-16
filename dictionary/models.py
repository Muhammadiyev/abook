from django.db import models

class Edition(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return "%s" %self.name
		
class Author(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	midname = models.CharField(max_length=100)
	birthDate = models.DateField(max_length=100)
	biograhy = models.CharField(max_length=100)
	books = models.IntegerField()
	photo_url = models.CharField(max_length=100)

	def __str__(self):
		return "%s" %self.firstname

	class Meta:
	        verbose_name = 'Автор'
	        verbose_name_plural = 'Авторы'



class Genre(models.Model):
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name}"

	class Meta:
	        verbose_name = 'Книга'
	        verbose_name_plural = 'Добавить жанры'



class Languages(models.Model):
	name_en = models.CharField(max_length=100)
	name_uz = models.CharField(max_length=100)
	name_ru = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name_ru}"