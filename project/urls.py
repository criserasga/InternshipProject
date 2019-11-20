from django.urls import path
from project import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.log_message, name="log"),
]

urlpatterns += staticfiles_urlpatterns()