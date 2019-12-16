from django.urls import path
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
	path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),

	path('register/', views.register, name='register'),
]