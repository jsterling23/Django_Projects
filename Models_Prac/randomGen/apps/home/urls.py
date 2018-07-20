from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_thoughts$', views.add_thoughts, name='add_thoughts'),
    url(r'^edit_thought/(?P<thought_id>\d+)/$', views.edit_thought, name='edit_thought'),
    url(r'^process_edit_thought/(?P<thought_id>\d+)/$', views.process_edit_thought, name='process_edit_thought'),
    url(r'^process_add_thought$', views.process_add_thought, name='process_add_thought'),
    url(r'^delete_thought/(?P<thought_id>\d+)/$', views.delete_thought, name='delete_thought'),
]

