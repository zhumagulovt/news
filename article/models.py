from django.utils import timezone
from django.db import models


class Theme(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    theme = models.OneToOneField(Theme, on_delete=models.CASCADE, primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=40, unique_for_date='date')

    def __str__(self):
        return self.title

