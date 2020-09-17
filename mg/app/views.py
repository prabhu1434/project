from django.shortcuts import render, redirect
from .models import *
from .forms import *

def details(request,id=0):
    if(request.method=="GET"):
        if(id==0):
            form=employee()
            form_3=other()
        else:
            id_value=employee_details.objects.get(id=id)
            id_value_3=other_details.objects.get(id=id)                        
            form=employee(instance=id_value)
            form_3=other(instance=id_value_3)
        return render(request,'details.html',{"form":form,"form_3":form_3})
    else:
        if (id==0):
            form=employee(request.POST)
            form_3=other(request.POST)
        else:
            id_value=employee_details.objects.get(id=id)
            id_value_3=other_details.objects.get(id=id)
            form=employee(request.POST,instance=id_value)
            form_3=other(request.POST,instance=id_value_3)
        print(form.is_valid(),form_3.is_valid())
        if (form.is_valid()==True and form_3.is_valid()==True):
            form.save()
            form_3.save()
        all_data=employee_details.objects.all()
        all_data_3=other_details.objects.all()
        for i in range(1,(int(request.POST["totallength"]))+1):
            aa=education_details(qualification=request.POST["qualification"+str(i)],institute=request.POST["institute"+str(i)],year=request.POST["year"+str(i)],percent=request.POST["percent"+str(i)])
            aa.save()
        for i in range(1,(int(request.POST["totallength_1"]))+1):
            aa=experience_details(company=request.POST["company"+str(i)],from_date=request.POST["from_date"+str(i)],to_date=request.POST["to_date"+str(i)],position=request.POST["position"+str(i)],reason=request.POST["reason"+str(i)])
            aa.save()
        # return render(request,'details.html',{"form":form,"form_1":form_1,"form_2":form_2,"form_3":form_3,"employee_details":all_data,"education_details":all_data_1,"experience_details":all_data_2,"other_details":all_data_3})
        return redirect('/next/')
        
def home(request):
    return render(request,'view.html')


def next(request,id=0):
    if(request.method=="GET"):
        if(id==0):
            form_4=salary()
            form_5=account()
        else:
            id_value_4=salary_details.objects.get(id=id)
            id_value_5=account_details.objects.get(id=id)                        
            form_4=salary(instance=id_value_4)
            form_5=account(instance=id_value_5)
        return render(request,'salary.html',{"form_4":form_4,"form_5":form_5})
    else:
        if (id==0):
            form_4=salary(request.POST)
            form_5=account(request.POST)
        else:
            id_value_4=salary_details.objects.get(id=id)
            id_value_5=account_details.objects.get(id=id)
            form_4=salary(request.POST,instance=id_value_4)
            form_5=account(request.POST,instance=id_value_5)
        print(form_4.is_valid(),form_5.is_valid())
        if (form_4.is_valid()==True and form_5.is_valid()==True):
            form_4.save()
            form_5.save()
        all_data_4=salary_details.objects.all()
        all_data_5=account_details.objects.all()
        # return render(request,'salary.html',{"form_4":form_4,"form_5":form_5,"salary_details":all_data_4,"account_details":all_data_5})
        return redirect('/role/')
    


def role(request):
    return render(request,'role.html')


