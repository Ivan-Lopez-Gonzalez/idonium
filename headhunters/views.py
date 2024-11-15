from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ActionAgenda
# Create your views here.

class ActionAgenda_ListView(ListView):
    model = ActionAgenda
    template_name = 'actionagenda_list.html'
    context_object_name = 'action_agenda'

class ActionAgenda_CreateView(CreateView):
    model = ActionAgenda
    template_name = 'actionagenda_form.html'
    fields = ['headhunter', 'date', 'task', 'status', 'comments']
    success_url = reverse_lazy('actionagenda_list')

class ActionAgenda_DeleteView(DeleteView):
    model = ActionAgenda
    template_name = 'actionagenda_delete.html'
    success_url = reverse_lazy('actionagenda_list')

class ActionAgenda_UpdateView(UpdateView):
    model = ActionAgenda
    template_name= 'actionagenda_form.html'
    fields = ['headhunter', 'date', 'task', 'status', 'comments']
    success_url = reverse_lazy('actionagenda_list')

