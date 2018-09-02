from django.urls import path
from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
    url(r'(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    path('post_create', views.post_create, name='post_create'),
]

