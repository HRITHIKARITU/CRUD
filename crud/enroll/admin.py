from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')