from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^register$', views.register, name = 'register' ),
    url(r'^success$', views.success, name = 'success'),
    url(r'^login$', views.login, name = 'loginmethod' ),
    url(r'^logout$', views.logout, name = 'logout'),
    
]