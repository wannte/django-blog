from django.shortcuts import render

def post_list(request):
    return render(request, 'articles/post_list.html', {})



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
