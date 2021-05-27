from django.contrib import admin
from . import models

@admin.register(models.Thing1)
class Thing1Admin(admin.ModelAdmin):
    list_display = ("pk", "attr", )

@admin.register(models.Thing2)
class Thing2Admin(admin.ModelAdmin):
    list_display = ("pk", "attr", )

