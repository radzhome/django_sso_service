from django.urls import path
# from django.views.generic.base import TemplateView

from identity import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'login/', views.login, name='sso_login'),
    path(r'logout/', views.logout, name='sso_logout'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
