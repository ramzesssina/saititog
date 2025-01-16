from django.contrib import admin
from .models import *

@admin.register(Musician)
class TaskAdmin(admin.ModelAdmin):
    pass