from django.shortcuts import render
from django.http import HttpRequest as request

from django.views.generic import ListView, DetailView
from .models import Tag, Category, Resource, News

class TagListView(ListView):
    model = Tag
    template_name = 'news_aggregator/tag_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()


class ResourceListView(ListView):
    model = Resource
    template_name = 'news_aggregator/resource_list.html'
    context_object_name = 'resources'

    def get_queryset(self):
        return Resource.objects.all()


class CategoryListView(ListView):
    model = Category
    template_name = 'news_aggregator/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()


class NewsListView(ListView):
    model = News
    template_name = 'news_aggregator/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_aggregator/news_single.html'

