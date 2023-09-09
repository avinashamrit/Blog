from django.shortcuts import redirect, render
from BlogApp.models import BlogModel
from django.contrib import messages
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from BlogApp.forms import Add_blog_form

@login_required(login_url='login')
def home(request):
    blog = BlogModel.objects.all()
    return render(request,'home.html',{'blog':blog})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Alredy Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Alredy Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,
                                                last_name=last_name,
                                                username=username,
                                                email=email,
                                                password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'passwoed not matching...')
            return redirect('register')
            
    else:
        return render(request,'register.html')

def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username/password is incorrect!')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
@login_required(login_url='login')
def search(request):
    title= request.POST['Search']
    blog = BlogModel.objects.filter(Blog_Heading__icontains=title)
    return render(request,'home.html',{'blog':blog})

    
@login_required(login_url='login')
def add_blog(request):
    if request.method=='GET':
        form= Add_blog_form()
        return render(request,'add_blog.html',{'form':form})
    else:
        form= Add_blog_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
@login_required(login_url='login')
def about(request):
    return render(request,'about.html')
