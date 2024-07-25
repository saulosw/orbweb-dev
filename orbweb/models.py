from django.db import models

class UserProfile(models.Model):
    profile_pic = models.ImageField(upload_to='media/profile_pics/', blank=True, null=True)
    username = models.CharField(max_length=20, unique=True)
    bio = models.CharField(max_length=150)

    def __str__(self):
        return self.username

class UserPost(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    post_content = models.TextField(max_length=280)
    post_likes = models.IntegerField(default=0)
    post_comments = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.post_date}"

class DiscussionTopic(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title