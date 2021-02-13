from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, View

from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'


    def deleteArticleView(self, request, i):
        y = Article.objects.get(id=i)
        y.delete()
        return HttpResponseRedirect('/')


'''
def addArticleView(request):
    author = request.POST['author']
    title = request.POST['title']
    body = request.POST['body']
    new_item = Article(author = author, title = title, body = body)
    new_item.save()
    return HttpResponseRedirect('')

def deleteArticleView(request, i):
    y = Article.objects.get(id = i)
    y.delete()
    return HttpResponseRedirect()

'''
