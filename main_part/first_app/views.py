from django.shortcuts import render, redirect
from .models import userdata,products,latest_products
from django.contrib import messages, auth
from django.contrib.auth import authenticate,login
from django.db.models import Q

# Create your views here.

def signup(request):
    if 'username' in request.session:
        context = {
            'products': products.objects.all(),
            'la_products':latest_products.objects.all()
        }
        return render(request, 'home.html', context)

    return render(request, 'signup.html')

def signin(request):
    if 'username' in request.session:
        context = {
            'products': products.objects.all(),
            'la_products':latest_products.objects.all()
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'signin.html')

def home(request):
    if 'username' in request.session:
        context = {
            'products': products.objects.all(),
            'la_products':latest_products.objects.all()
        }
        return render(request, 'home.html', context)

    return redirect(signin)

def admin_panel(request):
    if request.user.is_authenticated:
        context = {
            'users' : userdata.objects.all()
        }
        return render(request, 'admin_panel.html', context)
    elif 'username' in request.session:
        context = {
            'products': products.objects.all(),
            'la_products':latest_products.objects.all()
        }
        
        # return render(request, 'home.html', context)

    if 'username' in request.session:
        context = {
            'users' : userdata.objects.all()
        }
        return render(request, 'admin_panel.html', context)

    return redirect(signin)

def add_user(request):
    return render(request,'add_user.html')

def update_user(request,id):

    context = {
        'users': userdata.objects.get(id=id)
    }

    return render(request,'update_user.html', context)


def reg_form_submission(request):
    if request.method == 'POST':
        if userdata.objects.filter(
            email = request.POST['email'], username = request.POST['username']
        ).exists():
            messages.error(request, "email or username already exist...!",extra_tags='email_exist')
            return render(request, 'signup.html')
        
        elif request.POST['pass1'] != request.POST['pass2']:
            return render(request, 'signup.html')        
        
        else:
            values = userdata(
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['pass1']
            )
            values.save()
            return render(request, 'signin.html')

    else:
        return render(request, 'signup.html')

def login_form_submit(request):


    if request.method == 'POST':
        user1 = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(request, username = user1, password = pass1)

        if user is not None:
            login(request,user)
            request.session['username'] = user1
            context = {
                'users' : userdata.objects.all()
            }

            return render(request, 'admin_panel.html', context)
        else:
            if userdata.objects.filter(
                username = request.POST['username'], password = request.POST['password']
            ).exists():
                request.session['username'] = request.POST['username']
                context = {
                    'products': products.objects.all(),
                    'la_products':latest_products.objects.all()
                }
                return render(request, 'home.html',context)

            else:
                messages.error(request, "username or password is incorrect...!",extra_tags='login_fail')
                return render(request, 'signin.html')
    return render(request, 'signin.html')



def add_user_form(request):
    if request.method == 'POST':
        if userdata.objects.filter(
            email = request.POST['email'], username = request.POST['username']
        ).exists():
            messages.error(request, "email or username already exist...!",extra_tags='email_exist')
            return render(request, 'add_user.html')
        
        elif request.POST['pass1'] != request.POST['pass2']:
            messages.error(request, "password doesnt match...!",extra_tags='confirm_pass')
            return render(request, 'add_user.html')        
        
        else:
            values = userdata(
                username = request.POST['username'],
                email = request.POST['email'],
                password = request.POST['pass1']
            )
            values.save()
            context = {
            'users' : userdata.objects.all()
            }
            return render(request,'admin_panel.html', context)

    else:
        return render(request, 'add_user.html')

def delete_user(request,id):
    view_data = userdata.objects.get(id=id)
    view_data.delete()
    context = {
            'users' : userdata.objects.all()
            }
    return render(request,'admin_panel.html', context)

def update_user_form(request,id):
    
    if request.method == 'POST':
        
        ex1 = userdata.objects.filter(id=id).update(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        context = {
        'users' : userdata.objects.all()
        }
        return render(request, 'admin_panel.html', context)
    else:

        return render(request,'update_user.html')


def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return render(request, 'signin.html')


def search_user(request):
    if request.method == "POST":
        searched = request.POST['searched']

        multiple_query = Q(Q(username__icontains=searched) | Q(email__icontains=searched))
        users = userdata.objects.filter(multiple_query)
        
        context = {
            'users': users
        }

    return render(request, 'admin_panel.html', context)

    
    
    

