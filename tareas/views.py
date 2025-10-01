from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarea

class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/tarea_list.html'
    context_object_name = 'tareas'
    ordering = ['-fecha_creacion']
    paginate_by = 10

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detail.html'
    context_object_name = 'tarea'

class TareaCreateView(CreateView):
    model = Tarea
    template_name = 'tareas/tarea_form.html'
    fields = ['titulo', 'descripcion', 'prioridad', 'fecha_limite']
    success_url = reverse_lazy('tareas:tarea_list')
    
    def form_valid(self, form):
        form.instance.vigente = True
        return super().form_valid(form)

class TareaUpdateView(UpdateView):
    model = Tarea
    template_name = 'tareas/tarea_form.html'
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    success_url = reverse_lazy('tareas:tarea_list')

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tareas:tarea_list')