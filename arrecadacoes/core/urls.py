from django.urls import path
from . import views 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('ongs/', views.ongs_view, name='ongs'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('doacao/', views.doacao_view, name='doacao'),
]