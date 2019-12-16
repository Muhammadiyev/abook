from django.db import models
from dictionary.models import Genre, Author, Edition, Languages


class Playlist(models.Model):
	name = models.CharField(max_length=100)
	files = models.CharField(max_length=100)
	def __str__(self):
		return "%s the playlist" %self.name


		
class Audio(models.Model):
	volume = models.IntegerField()
	lang = models.CharField(max_length=100)
	reader = models.CharField(max_length=100)
	id_Playlist = models.CharField(max_length=100)

	def __str__(self):
		return "%s" %self.volume


class Book(models.Model):
	genre = models.ForeignKey(Genre, blank=True, null=True, default=None,on_delete=models.CASCADE, related_name="books")
	name = models.CharField(max_length=100)
	publishing_house = models.CharField(max_length=100)
	publish_year = models.DateField(max_length=100)
	number_of_page = models.IntegerField()
	isnb = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to='user_img')
	main_mp3 = models.FileField(upload_to='media/',null=True,verbose_name="Plik audio", blank=True)
	author = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE)
	lang = models.ForeignKey(Languages, blank=True, on_delete=models.CASCADE)
	id_Audio = models.ForeignKey(Audio, blank=True, on_delete=models.CASCADE)
	id_Edition = models.ForeignKey(Edition, blank=True, on_delete=models.CASCADE)
	dimensions = models.CharField(max_length=100)
	weight = models.IntegerField()

	def __str__(self):
		return "%s" %self.name
	
	class Meta:
	        verbose_name = 'Книга'
	        verbose_name_plural = 'Добавить книги'