from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add/',views.patient,name='patient'),
    path('viewall/',views.patient_list,name='patient_list'),
    path('view/<id>',views.patientdetail,name='patientdetail'),
    path('pcode/<patient_code>',views.patientcode,name='pcode'),
    path('',views.addpatient,name='addpatient'),

    
]