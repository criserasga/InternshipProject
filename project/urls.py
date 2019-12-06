# 
# This file contains all webpage URLs
# 

from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.sales_sheet, name="sales_sheet"),
    path("/", views.sales_sheet, name="sales_sheet")
    path("submit/", views.submit, name="submit"),
]

urlpatterns += staticfiles_urlpatterns()