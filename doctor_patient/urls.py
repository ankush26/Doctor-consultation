from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('view/<int:id>', views.view, name='view'),
    path('pr', views.patientRegistration, name='patientRegistration'),
    path('pl', views.patientLogin, name='patientLogin'),
    path('admin', views.adminLogin, name='adminLogin'),
    path('aLogin', views.aLogin, name='aLogin'),
    path('aLogout', views.aLogout, name='aLogout'),
    path('home/<str:spec>', views.specialization, name='spec'),
]