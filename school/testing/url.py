from django.urls import path
from  .import views

urlpatterns = [
     path("",views.home),
    path("about/",views.about),
    path("blog/",views.blog),
    path("contact/",views.contact)
]