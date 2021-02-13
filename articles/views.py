from django.shortcuts import render
from django.utils import timezone
from .models import Article


def post_list(request):
    posts = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles/post_list.html', {'posts': posts})


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
