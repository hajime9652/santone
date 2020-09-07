from django.contrib import admin

from . import models

admin.site.register(models.Tone)
admin.site.register(models.User)
admin.site.register(models.Room)

# Register your models here.
