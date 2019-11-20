from django.urls import path
from project import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.form, name="sales_sheet"),
]

urlpatterns += staticfiles_urlpatterns()