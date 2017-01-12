from django.shortcuts import render, HttpResponse
from django.utils import timezone
# import datetime


# Create your views here.
def index(request):
    # i = datetime.datetime.now()
    # currentDateTime = ("%s/%s/%s" % (i.month,i.day,i.year)) + (" %s:%s:%s" % (i.hour-5,i.minute,i.second))
    #
    # context = {
    # "currentDateTime":currentDateTime
    # }
    now = timezone.now()
    context = {
        'now': now
    }
    return render(request, 'timedisplay/index.html', context)
