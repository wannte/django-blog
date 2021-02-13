from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article


def post_list(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/post_detail.html', {'post': post})
