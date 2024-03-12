from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
    .filter(status=Post.Status.published)
class Post(models.Model):

    class Status(models.TextChoices):
        published = 'PB', 'Published'
        draft = 'DF', 'Draft'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices,
                              default=Status.draft)
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]


