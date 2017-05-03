from django.conf.urls import url
from . import views

app_name = 'Temperature'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^temperature/', views.input, name='input'),
    url(r'^temperature/add/$', views.RecordTemp.as_view(), name='record-temp'),
]