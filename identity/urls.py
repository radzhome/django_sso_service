from django.urls import path

from identity import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'login/', views.login, name='sso_login'),
    path(r'logout/', views.logout, name='sso_logout'),
    path(r'hidden/', views.hidden, name='hidden_frame'),
]
