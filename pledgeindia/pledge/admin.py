from django.contrib import admin

from .models import Pledge, User, UserPledges

# Register your models here.

admin.site.register(User)
admin.site.register(Pledge)
admin.site.register(UserPledges)
