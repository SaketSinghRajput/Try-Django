from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<my_id>/', ArticleListView.as_view(), name='article-list'),

]
