from django.contrib import admin
from . import models

# admin.site.register(models.Usuario)  # Remove or comment out this line
admin.site.register(models.Cliente)
admin.site.register(models.Loja)

