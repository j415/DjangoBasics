from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("sunck is a good man!")

def detail(request, num, num2):
    return HttpResponse('detail-%s-%s'% (num,num2))

from .models import Grades
def grades(request):
    #去模板里取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板,模板再渲染给页面，将渲染好的页面返回浏览器
    return render(request, "myApp/grades.html", {'grades': gradesList})

from .models import Students
def students(request):
    studentList = Students.objects.all()
    return render(request, "myApp/students.html", {"students": studentList})

def gradesStudents(request, num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html', {'students':studentsList})