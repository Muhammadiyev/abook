from django.contrib import admin
from .models import Cart



class Cartdmin(admin.ModelAdmin):
	list_display = [field.name for field in Cart._meta.fields]
	
	class Meta:
		model = Cart

admin.site.register(Cart, Cartdmin)


