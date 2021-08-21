from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add/',views.doctor,name='doctor'),
    path('viewall/',views.doctors_list,name='doctors_list'),
    path('view/<id>',views.doctordetail,name='doctordetail'),
    path('dcode/<fetchid>',views.doctorcode,name='dcode'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),

]

