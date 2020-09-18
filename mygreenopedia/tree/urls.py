from django.urls import path
from . import views 
app_name='tree'

urlpatterns = [
    
    path('', views.tree_list, name='listing'),
    path('<int:t_id>/', views.tree_detail, name='detailing'),
    path('<initial>/', views.tree_filter, name='filtering'),
   
]