from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login ,logout
from django.urls import reverse
from empapp.models import empdet
from empapp.forms import EmployeeForm

def login_r(request):

    return render(request, 'login.html')



def login_v(request):


    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user_obj = authenticate(request,username = username,password = password)
        if user_obj is not None:
            login(request,user_obj)
            return redirect(reverse("emp"))
        return redirect("/")

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return  redirect('/show')
            except:
                    pass
    else:
        form = EmployeeForm()
    return render(request,'emphome.html',{'form':form})

def show(request):
    Employee = empdet.objects.all()
    return render(request,"show.html",{'Employees':Employee})

def delete(request,id):
    Employee = empdet.objects.get(id=id)
    Employee.delete()
    return redirect("/show")

def p_logout(request):
    logout(request)
    return redirect("/")