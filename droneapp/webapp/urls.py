from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^/home.html$', views.index, name="index"),
    url(r'^/history.html$', views.history, name="history"),
    url(r'^/adds.html$', views.adds, name="adds"),
    #url(r'^contact/$', views.contact, name='contact'),
]
