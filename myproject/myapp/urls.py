from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('',views.index,name='index'),
    path('counter',views.counter,name = 'counter'),
    path('register',views.register,name = 'register'),
    path('detail',views.detail,name = 'detail'),
    path('addpatient',views.addpatient,name = 'addpatient'),
    path('check',views.check,name='check'),
    path('profil',views.profil,name='profil'),
    path('delete',views.delete,name='delete'),
    path('patient-profil/<int:patientid>/', views.profilpatient, name='profilpatient'),
    path('createcons/', views.createcons, name='createcons'),
    path('modify/', views.modify, name='modify'),
    path('deletepatient/', views.deletepatient, name='deletepatient'),
    path('conslist/', views.conslist, name='conslist'),
    path('pages-contact/', views.pagescontact, name='pages-contact'),
    # Autres routes
]
