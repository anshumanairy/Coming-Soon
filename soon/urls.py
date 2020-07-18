from django.urls import path
from django.conf.urls import url,include

from soon.controller import home

urlpatterns = [
    url(r'^$',home.home,name="home"),
]
