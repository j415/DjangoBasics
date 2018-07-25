from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    #return HttpResponse("kaishen is a good man")
    return render(request,'myApp/index.html')

from .models import Students
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request, "myApp/students.html",{"students":studentsList})

def students2(request):
    #报异常
    studentsList = Students.stuObj2.get(sgender=True)
    return HttpResponse("..................")

#显示前5条学生
def students3(request):
    studentsList = Students.stuObj2.all()[0:5]
    return render(request, "myApp/students.html", {"students": studentsList})

#分页显示学生
def stupage(request, page):
    #0-5   6-10   11-15
    # 1     2       3
    #page*5
    page = int(page)
    studentsList = Students.stuObj2.all()[(page-1)*5:page*5]
    return render(request, "myApp/students.html", {"students": studentsList})
from django.db.models import Max
def studentsearch(request):
    # studentsList = Students.stuObj2.filter(sname__contains="李")
    # studentsList = Students.stuObj2.filter(sname__startswith="李")
    # studentsList = Students.stuObj2.filter(sname__endswith="智")
    # studentsList = Students.stuObj2.filter(pk__in=[2,4,6,8,10])
    # studentsList = Students.stuObj2.filter(sage__gte=30)
    # studentsList = Students.stuObj2.filter(lastTime__year=2018)
    # studentsList = Students.stuObj2.filter(sname__contains="李%")
    studentsList = Grades.objects.filter(students__scontend__contains="刘德华")
    print(studentsList)
    # maxAge = Students.stuObj2.aggregate(Max('sage'))
    # print(maxAge)
    # studentsList = Students.stuObj2.filter(Q(pk__lte=3) | Q(sage__gt=50))  #Q对象获取或的关系，只有一个Q对象，就是用于匹配的
    # studentsList = Students.stuObj2.filter(Q(pk__lte=3))                   #只有一个Q对象，就是用于匹配的
    # studentsList = Students.stuObj2.filter(~Q(pk__lte=3))                    #取反
    return render(request, "myApp/students.html",{"students":studentsList})

from .models import Grades
def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("刘德华",34,True,"我叫刘德华，请多关照",grade,"2017-8-10","2017-8-11")
    stu.save()
    return HttpResponse('ddd')

def addstudent2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj2.createStudent("张学友",55,True,"我叫张学友，凯哥帅",grade,"2017-8-10","207-8-11")
    stu.save()
    return HttpResponse('*********')

from django.db.models import F,Q
def grades(request):
    # g =Grades.objects.filter(ggirlnum__gt=F('gboynum') +20) F对象获取对比的关系
    # print(g)
    # Students.stuObj2.filter(Q(pk__lte=3) | Q(sage__gt=50))
    return HttpResponse("00000000000000000")