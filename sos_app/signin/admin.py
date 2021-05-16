# Register your models here.
from django.contrib import admin

from .forms import User


class CaseAdmin(admin.ModelAdmin):
    pass


admin.register(User, CaseAdmin)