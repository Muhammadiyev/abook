from django.urls import path
from . import views

urlpatterns = [
	path('genre/<genre_id>/', views.HomePageView, name='genre'),
    path('', views.Home, name='home'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('book/<int:pk>/', views.CreateNewsView.as_view(), name='book'),
]