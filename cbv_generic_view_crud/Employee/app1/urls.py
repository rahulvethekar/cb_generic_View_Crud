from django.urls import path
from .views import EmployeeCreateView,EmployeeListView,EmployeeUpdateView,EmployeeDeleteView
urlpatterns=[
    path('employeeCreate/',EmployeeCreateView.as_view(),name='employeeCreate'),
    path('list/',EmployeeListView.as_view(),name='employeeList'),
    path('<int:pk>/Update/',EmployeeUpdateView.as_view(),name='employeeUpdate'),
    path('<int:pk>/Delete/',EmployeeDeleteView.as_view(),name='employeeDelete'),



]