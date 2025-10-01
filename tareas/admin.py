from django.contrib import admin
from .models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'prioridad', 'vigente', 'fecha_creacion', 'fecha_limite')
    list_filter = ('prioridad', 'vigente', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Estado y Prioridad', {
            'fields': ('prioridad', 'vigente')
        }),
        ('Fechas', {
            'fields': ('fecha_limite',)
        }),
    )