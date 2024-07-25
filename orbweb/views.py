from django.shortcuts import render
from .models import UserPost, DiscussionTopic

def home(request):
    posts = UserPost.objects.all().order_by('-id')
    top_disc_posts = DiscussionTopic.objects.all().order_by('-comments')[:3]

    return render(request, 'orbweb/pages/home.html', context={
        'posts': posts,
        'disc_posts': top_disc_posts,
    })

def discussion(request):
    disc_posts = DiscussionTopic.objects.all().order_by('-id')
    return render(request, 'orbweb/pages/discussion.html', context={
        'disc_posts': disc_posts,
    })