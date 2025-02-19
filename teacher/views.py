from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag



class Home(ListView):
    model = Post
    template_name = 'teacher/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context

def index(request):
    return render(request, 'teacher/index.html')

def get_category(request, slug):
    return render(request, 'teacher/category.html')

def get_post(request, slug):
    return render(request, 'teacher/category.html')