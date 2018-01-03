# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render_to_response, render, get_object_or_404
from django.template import RequestContext

from wiki.models import Article, Edit
from wiki.forms import ArticleForm, EditForm

import random

"""
@login_required
def add_article(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        msg = "Article saved successfully"
        messages.success(request, msg, fail_silently=True)
        return render(request, article.get_absolute_url(), { 'messages' : messages })
    return render(request, 'wiki/article_form.html', 
                              { 'form': form },)
"""

@method_decorator(login_required, name='dispatch')
class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'text', 'is_published', 'image_head']

    template_name = 'wiki/article_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Article saved successfully')
        form.instance.author = self.request.user
        return super(ArticleCreate, self).form_valid(form)

    def dispatch(self, *args, **kwargs):
        return super(ArticleCreate, self).dispatch(*args, **kwargs)

class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'wiki/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_articles = Article.published.exclude(slug=self.kwargs['slug'])

        articles_list = []  # A list to store related articles displayed in article page
        for article_num in range(1, 4):
            random_article = random.choice(published_articles)
            articles_list.append(random_article)
            published_articles = published_articles.exclude(slug=random_article.slug)

        context['articles_list'] = articles_list
        return context

"""
        
            context['RA'] = random.choice(random_articles)
"""

"""
@login_required
def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    edit_form = EditForm(request.POST or None)
    if form.is_valid():
        article = form.save()
        if edit_form.is_valid():
            edit = edit_form.save(commit=False)
            edit.article = article
            edit.editor = request.user
            edit.save()
            msg = "Article updated successfully"
            messages.success(request, msg, fail_silently=True)
            return redirect(article)
    return render_to_response('wiki/article_form.html', 
                              { 
                                  'form': form,
                                  'edit_form': edit_form,
                                  'article': article,
                              },)
"""

@method_decorator(login_required, name='dispatch')
class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'text', 'is_published', 'image_head']

    template_name = 'wiki/article_form.html'

    def dispatch(self, *args, **kwargs):
        return super(ArticleUpdate, self).dispatch(*args, **kwargs)

"""
def article_history(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return  object_list(request, 
                        queryset=Edit.objects.filter(article__slug=slug),
                        extra_context={'article': article})
"""

class ArticleList(ListView):
    model = Article
    context_object_name = 'all_articles'

    template_name = 'wiki/article_list.html'