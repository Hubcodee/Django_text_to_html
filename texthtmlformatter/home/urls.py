from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("input",views.inputfile,name="input"),
    path("result",views.result,name="result"),
]