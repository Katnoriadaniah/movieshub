from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import postform



class HomeView(ListView):
	model = Post
	template_name = 'Home.html'
	ordering = ['-id']



class DetailView(DetailView):
	model = Post
	template_name = 'mainfiles/detail.html'

class AddView(CreateView):
	model = Post
	form_class = postform
	template_name = 'mainfiles/addpost.html'
	#fields = '__all__'

class EditView(UpdateView):
	model = Post
	form_class = postform
	template_name = 'mainfiles/update.html'
	#fields = '__all__'

class DeleteView(DeleteView):
	model = Post
	template_name = 'mainfiles/delete.html'
	success_url = reverse_lazy('home')

class BollywoodView(ListView):
	model = Post
	template_name = 'category/bollywood.html'
	ordering = ['-id']

class HollywoodView(ListView):
	model = Post
	template_name = 'category/hollywood.html'
	ordering = ['-id']

class PunjabiView(ListView):
	model = Post
	template_name = 'category/punjabi.html'
	ordering = ['-id']

class SouthView(ListView):
	model = Post
	template_name = 'category/southindian.html'
	ordering = ['-id']



def contactus(request):
	return render(request, 'About/contactus.html')

def aboutus(request):
	return render(request, 'About/aboutus.html')




def SearchView(request):
	post = Post.objects.all()
	if request.method == 'POST':
		search = request.POST['search']
		result = Post.objects.filter(Q(title__icontains= search))
		return render(request,'ecomm/search.html', {'search':search,  'result':result})

	else:
		return render(request,'ecomm/search.html')

