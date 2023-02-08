from django.conf.urls import url
from . import views
from django.urls import path
from .views import FileListCreate
urlpatterns =[
    url(r'^$', views.index, name='index'),
    path(r'^file/', FileListCreate.as_view(), name='file-list-create')
]

