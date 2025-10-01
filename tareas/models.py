from django.db import models

class Tarea(models.Model):
    # Choices para prioridad
    PRIORIDAD_ALTA = 1
    PRIORIDAD_MEDIA = 2
    PRIORIDAD_BAJA = 3
    
    PRIORIDAD_CHOICES = [
        (PRIORIDAD_ALTA, 'Alta'),
        (PRIORIDAD_MEDIA, 'Media'),
        (PRIORIDAD_BAJA, 'Baja'),
    ]
    
    titulo = models.CharField(max_length=120, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción', blank=True)
    prioridad = models.IntegerField(
        choices=PRIORIDAD_CHOICES,
        default=PRIORIDAD_BAJA,
        verbose_name='Prioridad'
    )
    vigente = models.BooleanField(default=True, verbose_name='Vigente')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_limite = models.DateField(null=True, blank=True, verbose_name='Fecha límite')

    def __str__(self):
        return str(self.titulo) if self.titulo else "Tarea sin título"

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-fecha_creacion']