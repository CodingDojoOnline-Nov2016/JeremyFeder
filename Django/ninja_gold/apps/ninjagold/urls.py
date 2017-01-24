from django.conf.urls import url
from views import index, process

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^process_gold$', process, name='process_g'),
]
