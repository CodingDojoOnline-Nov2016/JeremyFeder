from django.conf.urls import url
from views import index, process, logout

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^process_gold$', process, name='process_g'),
    url(r'^logout$', logout, name='logout'),
]
