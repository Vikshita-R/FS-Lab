from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("program1/", views.program1, name="Program1"),
    path("program2/", views.program2, name="Program2"),
    path("program3/", views.program3, name="Program3"),
    path("program4/", views.program4, name="Program4"),
    path("program4/home/", views.home, name="home"),
    path("program4/about_us/", views.about_us, name="about_us"),
    path("program4/contact_us/", views.contact_us, name="contact_us"),
    
    path("program5/", views.program5, name="Program5"),
        
    path("program6/", views.program6, name="Program6"),
    path("program6/student_register/", views.student_register, name="student_register"),
    path("program6/course_register/", views.course_register, name="course_register"),
    
    path("program7/", views.program7, name="Program7"),
    
    path("program8/", views.program8, name="Program8"),
    path("program8/<int:pk>/", views.student_detail, name='student_detail'),
    path("program9/", views.program9, name="Program9"),
    path("program10/", views.program10, name="Program10"),
    path("program11/", views.program11, name="Program11"),

]
