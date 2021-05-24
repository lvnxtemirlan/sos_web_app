# Register your models here.
from django.contrib import admin

from .forms import User, Picture


class CaseAdmin(admin.ModelAdmin):
    pass


admin.register(User, CaseAdmin)

admin.register(Picture, CaseAdmin)