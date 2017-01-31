from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib import messages
import random
from .models import Leaderboard


# Create your views here.
def index(request):
    context = {
    'leaderboards': Leaderboard.objects.all().order_by('-top_score')[:5],
    # 'top_leaders': Leaderboard.objects.all(),
    }
    print Leaderboard.objects.all()
    return render(request, 'integration/index.html', context)

# def show(request):
#     print "I am SHOW!!!!!!!"
#     return render(request, 'integration/index.html', context)
