from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^menu/(?P<pk>\d+)/$', views.menu_detail, name='menu_detail'),
]