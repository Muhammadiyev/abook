from django.contrib import admin
from .models import Genre,Author,Edition,Languages



admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Edition)
admin.site.register(Languages)