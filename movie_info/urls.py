from django.conf.urls import url
from . import views
from .models import Movie, Category, Relationship

urlpatterns = [
    url(r'^(?P<movie_id>\d+)/$',views.detail,name='movie_detail'),
    url(r'^filter_sort', views.filter_sort, name='filter_sort'),
    url(r'^$', views.index, name='index'),
    ]

