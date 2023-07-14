from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth.forms import AuthenticationForm , authenticate , UserCreationForm 
from .forms import RegisterForm , PostForm
from django.urls import reverse_lazy
from django.contrib.auth import login , logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post
 
@login_required(login_url="/login")
def home_view(request):
    postsquery = Post.objects.all()
    posts = postsquery.order_by('-Created_At')
    return render(request , 'main/home.html' , {'posts':posts})

def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            username = user.get_username()  
            context = {
                'username' : username
            }
            return redirect(home_view)
        else:
            form = RegisterForm()
    else:
        form = RegisterForm()
    return render(request , 'registration/sign_up.html' , {'Form':form})

@login_required(login_url='login')
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()
    return render(request , 'main/create_post.html' , {'form':form})
