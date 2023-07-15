"""expressway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='index'),
    path('contact/',contact_us,name='contact'),
    path('about/',about,name='about'),
    path('order/', Order, name='order'),
   
    path('conf/',conf,name='conf'),

    path('',home,name="home"), #change here
    path('register',register,name="register"),
    path('reg/',reg,name="reg"),
    path('signin',signin,name="signin"),
    path('signout',signout,name="signout"),

    path('/admin2/dash/',dash,name='dashboard'),

    path('/menu/ins/',menu_form,name='menu_insert'),
    path('/menu/li/',menu_list,name='menu_list'),
    path('/menu/ins/<int:id>/',menu_form,name='menu_update'),
    path('/menu/delete/<int:id>/',menu_delete,name='menu_delete'),

   
    path('/order/li/',order_list,name='order_list'),
    path('/order/ins/<int:id>/',order_form,name='order_update'),
    path('/order/delete/<int:id>/',order_delete,name='order_delete'),

    path('/con/li/',con_list,name='con_list'),
    path('/con/delete/<int:id>/',con_delete,name='con_delete'),

    path('/admin2/login/',adm_log,name='adm_log'),
    path('ad/',ad,name='ad'),

    path('/adm/ins/',adm_form,name='adm_insert'),
    path('/adm/li/',adm_list,name='adm_list'),
    path('/adm/ins/<int:id>/',adm_form,name='adm_update'),
    path('/adm/delete/<int:id>/',adm_delete,name='adm_delete'),

    path('/user1/li/',user_list,name='user_list'),
    path('/user1/delete/<int:id>/',user_delete,name='user_delete'),


    
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 