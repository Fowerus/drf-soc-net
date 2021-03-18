from django.contrib import admin

from .models import *


admin.site.register(Community)
admin.site.register(CommunityCategory)
admin.site.register(Community_admins)
admin.site.register(Community_followers)
admin.site.register(CommunityPosts)
admin.site.register(CommunityPostLikes)
admin.site.register(CommunityPostComments)
