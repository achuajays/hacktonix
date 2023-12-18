"""
URL configuration for hacktonix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path , include
from chatapp import views
from app import views as view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('chat/', views.chat, name='chat'),
    path('view_messages/<int:sender_id>/<int:receiver_id>/', views.view_messages, name='view_messages'),
    path('user_details/<int:user_id>/', views.user_details, name='user_details'),
    path('send_message/<int:sender_id>/<int:receiver_id>/', views.send_message, name='send_message'),



    path('',view.home,name="home"),
]
