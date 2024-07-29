from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegisterForm

def signin(request):
    user_form_data = request.session.get('user_form_data')
    forms = RegisterForm(user_form_data)
    return render(request, 'users/pages/signin.html', context={
        'forms': forms,
    })

def signin_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['user_form_data'] = POST
    form = RegisterForm(POST)

    return redirect('user:signin')