from django.shortcuts import render, HttpResponse, get_object_or_404

import datetime
from datetime import timedelta

from . models import Fruit, Student

from . models import Course, Student5
# Create your views here.

def index(request):
    return render(request, "main/index.html")

def program1(request):
    now = datetime.datetime.now()
    data = {
        'now' : now,
    }
    return render(request, "main/program1.html", data)

def program2(request):
    now = datetime.datetime.now()
    offset_hours = 4
    
    four_hours_ahead = now + timedelta(hours=offset_hours)
    four_hours_before = now - timedelta(hours=offset_hours)  
    
    data = {
        'now': now,
        'four_hours_ahead': four_hours_ahead,
        'four_hours_before': four_hours_before,
    } 
    return render(request, "main/program2.html", data)

def program3(request):
    fruits = Fruit.objects.all()
    students = Student.objects.filter(selected = True)
    data = {
        'fruits': fruits,
        'students': students,
    }
    return render(request, "main/program3.html", data)

def program4(request):
    return render(request, "main/program4.html")

def home(request):
    return render(request, "main/home.html")

def about_us(request):
    return render(request, "main/about_us.html")

def contact_us(request):
    return render(request, "main/contact_us.html")

# def program5(request):
#     if request.method == "POST":
        
#         name=request.POST["sname"]
#         email=request.POST["email"]
#         course=request.POST["course"]
    
#         #for viewing list of students based on course
#         course_select = request.POST["course"]
#         student_list = Student5.objects.filter(id=course_select)
#         data = {
#             'student_list': student_list,
#         }
        
#         course = Course.objects.get(id=course)
        
#         student = Student5.objects.create(
#             name=name,
#             email=email,            
#         )
#         student.courses.set([course])
        
#         return render(request, "main/course-student2.html", data)
#     else:
#         courses = Course.objects.all()
#         data = {
#             'courses': courses,
#         }
#         return render(request, "main/program5.html", data)
    
# def course_student(request):
#     if request.method == "POST":
#         course_select = request.POST["course"]
        
#         student_list = Student5.objects.filter(id=course_select)
        
#         data = {
#             'student_list': student_list,
#         }
#         return render(request, "main/course-student2.html", data)
    
#     else:
#         return render(request, "main/course-student.html")

def program5(request):
    if request.method == "POST":
        
        name = request.POST.get("sname", "")
        email = request.POST.get("email", "")
        course_id = request.POST.get("course", None)
        course_select_id = request.POST.get("course_select", None)
        
        data = {}

        if course_select_id:
            # For viewing list of students based on course
            student_list = Student5.objects.filter(courses__id=course_select_id)
            data['student_list'] = student_list

        if name and email and course_id:
            course = Course.objects.get(id=course_id)
            student = Student5.objects.create(
                name=name,
                email=email,            
            )
            student.courses.set([course])

        return render(request, "main/course-student2.html", data)
    else:
        courses = Course.objects.all()
        data = {
            'courses': courses,
        }
        return render(request, "main/program5.html", data)

def program6(request):
    return render(request, "main/program6.html")

def student_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        usn = request.POST.get('usn')

        # Validate the data (you can add more validation as needed)
        if not name or not email or not usn:
            return HttpResponse("All fields are required", status=400)

        # Create and save the Student5 object
        Student5.objects.create(
            name = name,
            email = email,
            usn = usn
        )
        return HttpResponse("Student Registered Successfully!", status=400)
    else:
        return render(request, "main/student_register.html")

def course_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        text = request.POST.get('text')
        
        if not name or not code or not text:
            return HttpResponse("All fields are required", status=400)
        
        Course.objects.create(
            name = name,
            code = code,
            text = text
        )
        return HttpResponse("Course Registered Successfully!", status=400)
    else:
        return render(request, "main/course_register.html")

def program7(request):
    return render(request, "main2/index.html")

def program8(request):
    studentList = Student5.objects.all()
    data = {
        'studentList': studentList
    }
    return render(request, "main/program8.html", data)

def student_detail(request, pk):
    #student = get_object_or_404(Student5, pk=pk)
    student = Student5.objects.get(pk = pk)
    return render(request, 'main/student_detail.html', {'student': student})

def program9(request):
    return render(request, "main/program9.html")

def program10(request):
    return render(request, "main/program10.html")

def program11(request):
    return render(request, "main/program11.html")