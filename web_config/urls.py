"""web_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from home import views	as homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homeview.home, name="root"),
    path("list_rdb/", homeview.list_rdb, name='search_list_rdb'),
    path("list/", homeview.list, name='search_list'),
    path("home/", homeview.home, name="home"),
    path("export_csv/", homeview.export_csv, name="export_csv"),
    path("export_csv_rdb/", homeview.export_csv_rdb, name="export_csv_rdb"),
    path("attention_item/", homeview.attention_item),
    path('common/', include('common.urls')),

]
