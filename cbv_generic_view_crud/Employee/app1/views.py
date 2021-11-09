from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from .models import Employee
# Create your views here.

class EmployeeCreateView(CreateView):

    model = Employee
    fields = '__all__'
    success_url = '/list/'


class EmployeeListView(ListView):

    model = Employee



class EmployeeUpdateView(UpdateView):

    model = Employee
    fields = '__all__'
    success_url = '/list/'  




class EmployeeDeleteView(DeleteView):

    model = Employee
    success_url = '/list/'  








