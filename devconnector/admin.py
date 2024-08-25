from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserManager)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Post)
admin.site.register(Comment)