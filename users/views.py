from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from orbweb.models import UserProfile

def signin(request):
    user_form_data = request.session.get('user_form_data')
    form = RegisterForm(user_form_data)
    return render(request, 'users/pages/signin.html', context={
        'form': form,
    })

def signin_create(request):
    if request.method != 'POST':
        raise Http404()
    
    POST = request.POST
    request.session['user_form_data'] = POST
    form = RegisterForm(POST, request.FILES)
    
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        profile_pic = form.cleaned_data.get('profile_pic')
        bio = form.cleaned_data.get('bio')
        
        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(
            user=user,
            profile_pic=profile_pic,
            bio=bio
        )
        
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('home')
        
    return redirect('user:signin')
