from django.urls import path
from .views import home_view

urlpatterns = [path("", home_view.as_view(), name="index")]
