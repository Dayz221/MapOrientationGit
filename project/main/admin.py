from django.contrib import admin
from . import models

admin.site.register(models.Boards)
admin.site.register(models.Cards)
admin.site.register(models.Routes)
admin.site.register(models.Sessions)
admin.site.register(models.Users)
