from django.conf.urls import url
from wiki.models import Article
from wiki import views

urlpatterns = [
    url(r'^$', views.ArticleList.as_view(), name='wiki_article_index'),
    url(r'^article/(?P<slug>[-\w]+)$', views.ArticleDetail.as_view(), name='wiki_article_detail'),
    #url(r'^history/(?P<slug>[-\w]+)$', views.article_history, name='wiki_article_history'),
    url(r'^add/article/$', views.ArticleCreate.as_view(), name='wiki_article_add'),
    url(r'^edit/article/(?P<slug>[-\w]+)/$', views.ArticleUpdate.as_view(), name='wiki_article_edit'),
]
