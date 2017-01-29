from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib import messages
import random
from .models import Leaderboard


# Create your views here.
def index(request):
    return render(request, 'integration/index.html')

def show(request):
    context = {
        'leaderboards': Leaderboard.objects.all().order_by('-top_score')[:5],
        # 'top_leaders': Leaderboard.objects.all(),
    }
    return render(request, 'integration/index.html', context)
