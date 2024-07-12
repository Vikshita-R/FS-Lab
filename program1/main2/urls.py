from django.urls import path
from . import views

urlpatterns = [
    path("program7/", views.index, name="program7"),
    path("add_project/", views.add_project, name="add_project"),
    path("projectreg/", views.add_project1, name="projectreg"),
    path('enroll/', views.reg, name='enroll'),
    
]