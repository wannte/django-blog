from django.urls import path
from . import views
# from .views import deleteArticleView

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='detail'),
]
'''
path('deleteArticleItem/<int:pk>', deleteArticleView,
'''
