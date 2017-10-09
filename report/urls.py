"""report URL Configuration

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
from django.conf.urls import url
# import report.views
from report.views import charts, views
app_name ='report'
urlpatterns = [
    # url(r'^synchronous-report-current/', views.synchronous_report_current, name='current'),
    # url(r'^save-report/', views.save_report, name='save'),
    # url(r'^(?P<pk>[0-9]+)/synchronous-report/$', views.synchronous_report, name='synchronous_report'),
    url(r'^mrp-calculator/', views.mrp_calculator, name='mrp-calculator'),
    url(r'^dashboard/(?P<year>[0-9]+)/$', charts.dashboard, name='dashboard'),
    # url(r'^area/(?P<product>([\w& ]+))/$', charts.area, name='area'),
    url(r'^detail/(?P<product>([\w& -]+))/$', charts.detail, name='detail'),
    # url(r'^report-preview/', views.report_preview, name='report-preview'),
]
#
#synchronous-report