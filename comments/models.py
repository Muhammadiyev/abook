from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from books.models import Book


class Comment(models.Model):
	avtor = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
	text = models.TextField()
	date = models.DateTimeField(auto_now_add=True, auto_now=False)
	book = models.ForeignKey(Book, null=True, default=None, on_delete=models.CASCADE, related_name="comments")


	def get_absolute_url(self):
		return reverse('book', args=[int(self.pk)])


	def __str__(self):
		return "%s" %self.avtor
