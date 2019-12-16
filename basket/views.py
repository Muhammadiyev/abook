from django.shortcuts import render,redirect
from books.models import Book
from basket.models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.db.models import Sum
from dictionary.models import Genre


class BasketView(LoginRequiredMixin,DetailView):
	model = Book
	template_name = 'basket/count.html'

	def get_context_data(self, **kwards):
		current_user = self.request.user
		cxt = super(BasketView, self).get_context_data(**kwards)
		cxt['name'] = Book.objects.filter(pk=self.kwargs['pk']).first()
		cxt['count'] = Cart.objects.filter(user=current_user.username).count()
		cxt['genre'] = Genre.objects.filter()
		cxt['sum'] = Cart.objects.filter(user=current_user.username).aggregate(Sum('price'))
		return cxt 

def return_data(request):
	b = Cart(name=request.POST['text'], author=request.POST['author'],
		price=request.POST['price'], user=request.POST['user'],main_mp3=request.POST['main_mp3'])
	b.save()
	return redirect('/count/' + request.POST['id'])



def count(request):
	return render(request, 'basket/count.html')