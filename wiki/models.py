from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class PublishedArticlesManager(models.Manager):

    def get_queryset(self):
        return super(PublishedArticlesManager, self).get_queryset().filter(is_published=True)

class Article(models.Model):
    """Represents a wiki article"""

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    text = models.TextField()
    image_head = models.ImageField(upload_to='wiki/images/', default='wiki/images/phoenix-feather.png')
    author = models.ForeignKey(User, related_name='article_author')
    is_published = models.BooleanField(default=False, verbose_name="Publish")
    created_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    published = PublishedArticlesManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('wiki_article_detail', (), { 'slug' : self.slug })

class Edit(models.Model):
    """Stores an edit session"""

    article = models.ForeignKey(Article)
    editor = models.ForeignKey(User)
    edited_on = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length=100)

    class Meta:
        ordering = ['-edited_on']

    def __unicode__(self):
        return "%s - %s -%s" %(self.summary, self.editor, self.edited_on)

    def __str__(self):
        return "%s - %s -%s" %(self.summary, self.editor, self.edited_on)
    @models.permalink
    def get_absolute_url(self):
        return ('wiki_edit_detail', self.id)
