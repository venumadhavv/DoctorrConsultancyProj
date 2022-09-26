from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('5',views.ViewAllPatients,name='view'),
    path('Uregister/',views.patientregister,name='uregister'),
    path('Ulogin/',views.userlogin,name='ulogin'),
    path('Uedit/<str:pk>/',views.editprofie,name='uedit'),
    path('UviewProfile/<str:pk>/',views.viewprofile,name="uviewprofile"),


    path('Dlogin/',views.doctorlogin,name='dlogin'),
    path('Dregister/',views.doctorregister,name='dregister'),
    path('DviewProfile/<str:pk>/',views.doctorviewprofile,name="dviewprofile"),
    path('Dedit/<str:pk>/',views.doc_edit,name='dedit'),
]