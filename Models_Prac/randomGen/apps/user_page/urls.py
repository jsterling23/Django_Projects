from django.conf.urls import url 
from . import views

app_name = 'user_page'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit_bio/$', views.edit_bio, name='edit_bio'),
    url(r'^process_edit_bio/$', views.process_edit_bio, name='process_edit_bio'),
]