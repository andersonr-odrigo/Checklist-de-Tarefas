from django.urls import path
from .views import *

urlpatterns = [path("inicio/", home, name="inicio")]
