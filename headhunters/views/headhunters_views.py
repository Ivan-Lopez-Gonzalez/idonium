

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Headhunter
from ..forms import HeadhunterForm

class HeadhunterListView(ListView):
    model = Headhunter
    template_name = 'headhunters/headhunter_list.html'
    context_object_name = 'headhunters'

class HeadhunterDetailView(DetailView):
    model = Headhunter
    template_name = 'headhunters/headhunter_detail.html'
    context_object_name = 'headhunter'

class HeadhunterCreateView(CreateView):
    model = Headhunter
    form_class = HeadhunterForm
    template_name = 'headhunters/headhunter_form.html'
    success_url = reverse_lazy('headhunter_list')

class HeadhunterUpdateView(UpdateView):
    model = Headhunter
    form_class = HeadhunterForm
    template_name = 'headhunters/headhunter_form.html'
    success_url = reverse_lazy('headhunter_list')

class HeadhunterDeleteView(DeleteView):
    model = Headhunter
    template_name = 'headhunters/headhunter_confirm_delete.html'
    success_url = reverse_lazy('headhunter_list')
