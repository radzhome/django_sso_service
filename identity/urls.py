from django.urls import path
# from django.views.generic.base import TemplateView

from identity import views

urlpatterns = [
    path(r'login/', views.login, name='seo_login'),
    path(r'', views.home, name='home'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
