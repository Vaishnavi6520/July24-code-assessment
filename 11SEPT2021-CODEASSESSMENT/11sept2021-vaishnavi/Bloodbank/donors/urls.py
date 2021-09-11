from . import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('search/',views.search,name='search'),
    path('update/',views.update,name='update'),     
    path('viewdonor/',views.viewdonor,name='viewdonor'),     
    path('add/',views.donor,name='donor'),
    path('all/',views.donor_list,name='donor_list'),
    path('detail/<id>',views.donordetail,name='detail'),
    path('login_check/',views.login_check,name='login_check'),
    path('updateapi/',views.updatesearchapi,name='updatesearchapi'),
    path('updateApi/',views.update_data_read,name='update_data_read'),

]
