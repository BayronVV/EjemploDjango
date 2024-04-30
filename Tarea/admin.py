from django.contrib import admin
from .models import Pendiente
# Register your models here
@admin.register(Pendiente)
class PendienteAdmin(admin.ModelAdmin):
    list_display=('name', 'priority')
    ordering = ('priority','name')
    