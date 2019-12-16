from django.db import models


class Cart(models.Model):
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	user = models.CharField(max_length=100)
	main_mp3 = models.CharField(max_length=300)

	def __str__(self):
		return "Пользователь %s %s" % (self.user, self.name)

	class Meta:
	        verbose_name = 'Покубки'
	        verbose_name_plural = 'Покубки в корзине'