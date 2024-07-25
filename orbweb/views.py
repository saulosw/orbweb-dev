from django.shortcuts import render
from .models import UserPost, DiscussionTopic

def home(request):
    posts = UserPost.objects.all().order_by('-id')

    return render(request, 'orbweb/pages/home.html', context={
        'posts': posts,
    })

def discussion(request):
    disc_posts = DiscussionTopic.objects.all().order_by('-id')
    return render(request, 'orbweb/pages/discussion.html', context={
        'disc_posts': disc_posts,
    })