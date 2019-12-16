from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from basket import views as basketViews 
from users import views as userViews 
from django.contrib.auth import views as authViews 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', userViews.profile, name='profile'),
    path('count/', basketViews.count, name='count'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('', include('basket.urls')),
    path('', include('books.urls')),
    path('', include('dictionary.urls')),
    path('', include('users.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)