from django.urls import path
from .views import *
urlpatterns=[
    path('employee/create/',employee_create.as_view(),name='create'),
    path('employee/update/<int:pk>/',employee_update.as_view(),name='update'),
    path('employee/detail/<int:pk>/',employee_detail.as_view(),name='detail'),
    path('employee/delete/<int:pk>/',employee_delete.as_view(),name='delete'),
    path('',employee_list.as_view(),name='list'),
]