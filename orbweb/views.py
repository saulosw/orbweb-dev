from django.shortcuts import render
from .models import UserPost

def home(request):
    posts = UserPost.objects.all().order_by('-id')

    return render(request, 'orbweb/pages/home.html', context={
        'posts': posts,
    })

def discussion(request):
    return render(request, 'orbweb/pages/discussion.html')