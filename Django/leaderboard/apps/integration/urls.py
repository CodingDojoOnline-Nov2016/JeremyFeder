from django.conf.urls import url
# from . import views
from views import index, show

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^leaderboard$', show, name='leader'),
    # url(r'^register$', register, name='register'),
    # url(r'^success$', success, name='success'),
    # url(r'^logout$', logout, name='logout'),
]
