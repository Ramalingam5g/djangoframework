from . import views
from django.urls import path

urlpatterns = [    
    path('',views.home_view),
    path('material_list', views.material_List),
    path('create_material', views.create_Material),
    path('material_update/<uuid:id>', views.material_Update),
    path('main_list/<uuid:id>', views. material_View),
    path('master_page',views.master_Page),
    path('Create_Method',views.Create_Method),
    # path('',views.display),
    path('display/',views.display,name="display"),
    path('update/<str:id>', views.Update_Method)  
   
]