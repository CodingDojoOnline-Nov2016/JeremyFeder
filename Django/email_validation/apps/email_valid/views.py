from django.shortcuts import render, redirect, HttpResponse
from .models import Email

# Create your views here.
def index(request):
    return render(request, 'email_valid/index.html')

def create(request):
    if request.method == "POST":
        result = Email.emailManage.register(request.POST['email'])
        if result[0]:
            #Displays entered email as the validated email in Success
            request.session['email'] = result[1].email
            #Clears out session errors on "Back"
            request.session['errors'] = []
            return redirect('/success')
        else:
            ##Else there is an error
            request.session['errors'] = result[1]
            return redirect('/')
    else:
        return redirect('/')

def success(request):
    emails = Email.emailManage.all()
    return render(request, 'email_valid/success.html', {'emails':emails, 'your_email': request.session.get('email')})

def destroy(request, id):
    result = Email.emailManage.destroy(id)
    return redirect('/success')
