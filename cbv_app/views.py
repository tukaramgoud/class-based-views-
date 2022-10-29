from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import employee

class employee_create(CreateView):
    model = employee
    fields = '__all__'
    template_name = 'create.html'
    context_object_name = 'form'

class employee_update(UpdateView):
    model = employee
    fields = '__all__'
    template_name = 'create.html'
    context_object_name = 'form'

class employee_detail(DetailView):
    model = employee
    template_name = 'emp_detail.html'
    context_object_name = 'employee'

class employee_delete(DeleteView):
    model = employee
    success_url = 'create'
    template_name = 'emp_confirm_delete.html'
    context_object_name = 'employee'

class employee_list(ListView):
    model = employee
    fields='__all__'
    template_name = 'emp_list.html'
    context_object_name = 'employee'