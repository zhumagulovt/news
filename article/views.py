from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Article, Theme


def index(request):

    return render(request, 'article/index.html')


def get_time(request):
    print(timezone.timezone.utc)
    return HttpResponse(timezone.localtime())


def create_article(request):

    if request.method == 'POST':

        post_ = request.POST

        theme = Theme.objects.create(name=post_['theme'])

        art = Article.objects.create(
            title=post_['title'],
            content=post_['content'],
            theme=theme
        )
        print(art)
        return redirect('/create_article')
    else:
        return render(request, 'article/add_art.html')
