from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ActionAgenda_ListView.as_view(), name='actionagenda_list'),  
    path('nuevo/', ActionAgenda_CreateView.as_view(), name='actionagenda_create'),  
    path('<int:pk>/editar/', ActionAgenda_DeleteView.as_view(), name='actionagenda_update'),  
    path('<int:pk>/eliminar/', ActionAgenda_UpdateView.as_view(), name='actionagenda_delete'),  
]