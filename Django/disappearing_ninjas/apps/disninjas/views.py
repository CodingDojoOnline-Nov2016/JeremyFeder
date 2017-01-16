from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'disninjas/index.html')

def ninja(request):
    return render(request, 'disninjas/show.html')    

def show(request, ninja_color):
    turtles = {
        'purple': 'disninjas/images/donatello.jpg',
        'blue': 'disninjas/images/leonardo.jpg',
        'orange': 'disninjas/images/michelangelo.jpg',
        'red': 'disninjas/images/raphael.jpg',
    }
    if ninja_color in turtles:
        context = {
            'image': turtles[ninja_color]
        }
    else:
        context = {
            'image': 'disninjas/images/notapril.jpg'
        }
    return render(request, 'disninjas/show.html', context)
