from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Option)
admin.site.register(Poll)

# Register your models here.
