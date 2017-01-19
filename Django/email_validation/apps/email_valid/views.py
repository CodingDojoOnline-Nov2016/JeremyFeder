from django.shortcuts import render, redirect, HttpResponse
from .models import Email

# Create your views here.
def index(request):
    return render(request, 'email_valid/index.html')

def create(request):
    if request.method == "POST":
        result = Email.emailManage.register(request.POST['email'])
        if result[False]:
            request.session['email'] = result[True].email
            request.session['errors'] = []
            return redirect('/success')
        else:
            request.session['errors'] = result[True]
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    emails = Email.emailManage.all()
    return render(request, 'email_valid/success.html', {'emails':emails, 'your_email': request.session.get('email')})

def destroy(request, id):
    result = Email.emailManage.destroy(id)
    return redirect('/success')
