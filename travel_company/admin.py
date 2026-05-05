from django.contrib import admin
from . import models

admin.site.register(models.Person)
admin.site.register(models.Horse)
admin.site.register(models.TourCompany)
admin.site.register(models.Service)
admin.site.register(models.Review)
