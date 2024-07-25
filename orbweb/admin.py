from django.contrib import admin
from .models import UserPost, UserProfile, DiscussionTopic

class UserProfileAdmin(admin.ModelAdmin):
    ...

class UserPostAdmin(admin.ModelAdmin):
    ...

class DiscussionTopicAdmin(admin.ModelAdmin):
    ...

admin.site.register(UserPost, UserPostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(DiscussionTopic, DiscussionTopicAdmin)