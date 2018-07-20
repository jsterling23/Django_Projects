from django.conf.urls import url 
from . import views

app_name="quote_collector"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]