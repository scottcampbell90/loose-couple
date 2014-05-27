from django.contrib import admin
from models import Channel, UserProfile, PostModel
# Register your models here.

admin.site.register(UserProfile)

admin.site.register(Channel)

admin.site.register(PostModel)