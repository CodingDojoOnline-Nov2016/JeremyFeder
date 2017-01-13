from django.shortcuts import render, redirect
import random
# Create your views here.

def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
        request.session['word'] = 'Click GENERATE for a Random Word!'
    return render(request, 'rwg/index.html')

def create(request):
    random_word = ''
    letters = ['r','a','n','d','o','m','w','r']
    for i in range(12):
        letter_index = random.randint(0, len(letters) - 1)
        random_word += letters[letter_index]
    request.session['attempt'] += 1
    request.session['word'] = random_word
    print "9999999999 Create"
    return redirect('/')

def reset(request):
    del request.session['attempt']
    del request.session['word']
    print "8888888888 Destroy"
    return redirect('/')
