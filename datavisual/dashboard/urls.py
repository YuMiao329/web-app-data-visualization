from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('function1/', views.function1, name='function 1'),

 
  
 
    path('Import_csv/', views.Import_csv,name="Import_csv"), 
    path('parsed_csv_demo/', views.parsed_csv_demo,name="parsed_csv_demo"),
    path('parsed_csv_demo_2/', views.parsed_csv_demo_2,name="parsed_csv_demo_2"),
    path('product/', views.product,name="dashboard-product"),
    path('staff/', views.staff,name="dashboard-staff"),
    path('order/', views.order,name="dashboard-order"),
     

]