from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(req):
    if req.method=='POST':
        #Register User
        first_name=req.POST['first_name']
        last_name=req.POST['last_name']
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        password2=req.POST['password2']

        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(req,'That username is taken')
                return redirect('register')

            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(req,'That Email is being used')
                    return redirect('register')

                else:
                    ##looks good
                    user=User.objects.create_user(username=username,password=password,email=email,
                    first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(req,'You are now registered')
                    return redirect('login')
        
        else:
            messages.error(req,'Passwords do not match')
            return redirect('register')

    else:
        return render(req,'accounts/register.html')
# Create your views here.

def login(req):
    if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(req,user)
            messages.success(req,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(req,'Invalid username/Password')
            return redirect('login')
    else:
        return render(req,'accounts/login.html')


def logout(req):
    auth.logout(req)
    return redirect('index')

def dashboard(req):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=req.user.id)
    context={
        'contacts':user_contacts
    }
    return render(req,'accounts/dashboard.html',context)