from django.urls import path
from . import views


urlpatterns = [
	path('output', views.return_data),
    path('count/<int:pk>/', views.BasketView.as_view(), name='count-detail'),
	#path('contacti', views. .as_view(), name=''),
    #path('/<int:pk>/', views. .as_view(), name=''),
    #path('/<int:pk>/', views. .as_view(), name=''),
    #path('/<string>/', views. .as_view(), name=''),
]