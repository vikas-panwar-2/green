from django.urls import path
from . import views 
app_name='tree'

urlpatterns = [
    
    path('', views.tree_list, name='listing'),
    path('<t_id>/', views.tree_detail, name='detailing'),
   
]