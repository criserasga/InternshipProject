from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.sales_sheet, name="sales_sheet"),
]

urlpatterns += staticfiles_urlpatterns()