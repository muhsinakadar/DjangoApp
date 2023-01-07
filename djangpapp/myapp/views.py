from django.contrib import messages
from django.shortcuts import render, redirect

from myapp import form
from myapp.form import StudentForm
from django.http import HttpResponse
from myapp.functions import handle_uploaded_file
from myapp.form import StudentForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def hello(request):
    return render(request,"index.html")
def home(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request, "home.html", {'form': student})

def setsession(request):
    request.session['sname'] = 'irfan'
    request.session['semail'] = 'irfan.sssit@gmail.com'
    return HttpResponse("session is set")
def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+" "+studentemail);
def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response
def getcookie(request):
    tutorial  = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: "+  tutorial);


# def register(request):
#     if request.POST == 'POST':
#         form = UserCreationForm()
#         if form.is_valid():
#             form.save()
#     messages.success(request, 'Account created successfully')
#
#     else:
#         form = UserCreationForm()
#
#
#     context = {
#         'form': form
# #     }
# return render(request, 'register.html', context)

