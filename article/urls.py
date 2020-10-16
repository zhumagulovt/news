from django.urls import path

from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_art', views.create_article, name='add_art'),
    path('time', views.get_time)
]