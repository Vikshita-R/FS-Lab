from django.shortcuts import render, HttpResponse
from . models import Course, Student, ProjectReg, ProjectRegistration
# Create your views here.

def index(request):
    return render(request, "main2/index.html")

def reg(request): 
    if request.method == "POST": 
        sid = request.POST.get("sname") 
        cid = request.POST.get("cname") 
        student = Student.objects.get(id=sid) 
        course = Course.objects.get(id=cid) 
        res = student.enrolment.filter(id=cid) 
        if res: 
            return HttpResponse("<h1>Student already enrolled</h1>") 
        student.enrolment.add(course) 
        return HttpResponse("<h1>Student enrolled successfully</h1>") 
        
    else: 
        students = Student.objects.all() 
        courses = Course.objects.all()
        return render(request, "main2/t2.html", {"students": students, "courses": courses})

def add_project(request): 
    if request.method == "POST": 
        form = ProjectReg(request.POST) 
        if form.is_valid():
            form.save() 
            return HttpResponse("<h1>Record inserted successfully</h1>") 
        else: 
            return HttpResponse("<h1>Record not inserted</h1>") 
    else: 
        form = ProjectReg() 
        return render(request, "main2/index.html", {"form": form})

def add_project1(request): 
    if request.method == "POST": 
        form = ProjectRegistration(request.POST) 
        if form.is_valid():
            form.save() 
            return HttpResponse("<h1>Record inserted successfully</h1>") 
        else: 
            return HttpResponse("<h1>Record not inserted</h1>") 
    else: 
        form = ProjectRegistration() 
        return render(request, "main2/index.html", {"form": form})
