
from django.urls import path
from . import views


urlpatterns=[
    path("",views.index,name="hello/index.html"),
    path("<str:name>",views.greet,name="greet"),
    path("brian",views.brian,name="brain"),
    path("david",views.david,name="david"),
]