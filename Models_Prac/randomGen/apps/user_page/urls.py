from django.conf.urls import url 
from . import views

app_name = 'user_page'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]