from django.shortcuts import render
from dictionary.models import Genre
from basket.models import Cart
from django.views import View
from django.db.models import Sum, Q
from comments.models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, DetailView

def HomePageView(request,genre_id):

	book = Book.objects.filter(genre=genre_id).first()
	books = Book.objects.filter(genre=genre_id).all()
	genre = Genre.objects.all()
	count = Cart.objects.filter(user=request.user.username).count()
	sum = Cart.objects.filter(user=request.user.username).aggregate(Sum('price'))
	title = 'Жанры'
	return render(request, 'books/genre.html',locals())

def Home(request):
	data = {
		'count': Cart.objects.filter(user=request.user.username).count(),
		'sum': Cart.objects.filter(user=request.user.username).aggregate(Sum('price')),
		'new': Book.objects.filter(),
		'genre': Genre.objects.filter(),
		'title': 'Новые поступления'
	}
	return render(request, 'books/main.html',data)


class CreateNewsView(LoginRequiredMixin,CreateView):
	model = Book
	model = Comment
	context_object_name = 'comment'
	fields = ['text']
	template_name = 'books/books.html'

	def form_valid(self,form):
		form.instance.avtor = self.request.user
		return super().form_valid(form)


	def get_context_data(self, **kwards):
		current_user = self.request.user
		ctx = super(CreateNewsView, self).get_context_data(**kwards)
		ctx['book'] = Book.objects.filter(pk=self.kwargs['pk']).first()
		ctx['books'] = Book.objects.filter(pk=self.kwargs['pk']).all()
		ctx['count'] = Cart.objects.filter(user=current_user.username).count()
		ctx['genre'] = Genre.objects.filter()
		
		# book = Book.objects.filter(pk=self.kwargs['pk']).first()
		# ctx['comments'] = Comment.objects.filter(book_id=book).all()

		ctx['sum'] = Cart.objects.filter(user=current_user.username).aggregate(Sum('price'))
		return ctx 




class SearchView(ListView):
	model = Book
	template_name = 'books/search.html'

	def get_queryset(self):
		current_user = self.request.user
		queryset = Book.objects.all()

		q = self.request.GET.get('search')
		if q:
			return queryset.filter(Q(name__icontains=q) | Q(publishing_house__icontains=q))
		

	def get_context_data(self, **kwards):
		current_user = self.request.user
		ctx = super(SearchView, self).get_context_data(**kwards)
		ctx['count'] = Cart.objects.filter(user=current_user.username).count()
		ctx['sum'] = Cart.objects.filter(user=current_user.username).aggregate(Sum('price'))
		ctx['genre'] = Genre.objects.filter()

		return ctx

