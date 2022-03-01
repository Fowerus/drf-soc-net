from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(User_followers)

admin.site.register(UserPosts)
admin.site.register(UserPostLikes)
admin.site.register(UserPostComments)