from django.conf.urls import include, url
from . import views
from .views import *
urlpatterns = [

    url(r'^$', views.index, name='index')
    ]