from django.shortcuts import render

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    
)
from .models import Article  # Ensure this is the correct model

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    
    template_name = 'blog/article_list.html'

    queryset = Article.objects.all()