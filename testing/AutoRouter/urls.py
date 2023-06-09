"""testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import include, re_path
from django.contrib import admin
from .views import execute_script, home, new_router
from .login import login_render, fixme, secure
from .more_resources import more_resources
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path('execute_script/', execute_script, name='execute_script'),
    re_path('new_router/', new_router, name='new_router'),
    re_path(r'login', login_render, name='login'),
    re_path(r'fixme', fixme, name ='fixme'),
    re_path(r'secure', secure, name = 'secure'),
    re_path(r'more-resources', more_resources, name = 'more_resources'),
    re_path('', home, name='home'),
]
