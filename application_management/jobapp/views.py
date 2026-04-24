from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicantForm, ApplicationModelForm
from django.forms import modelform_factory
from .models import Application
from django.shortcuts import redirect

# Create your views here.
def home(request):
    applications = Application.objects.all()

    return render(request, 'jobapp/index.html', {'applications':applications})

def applications(request):
    # return HttpResponse("Hello World")
    if request.method == 'GET':
        # AppModelForm = modelform_factory(Application, fields="__all__")
        form = ApplicationModelForm()
        # form = AppModelForm()
        return render(request, 'jobapp/home.html', {'form':form})
    if request.method == 'POST':
        print(request.POST)
        form = ApplicationModelForm(request.POST)
        if form.is_valid():
            '''
            for accessing form data
            applicant_name = form.cleaned_data['applicant_name']
            print(applicant_name)'''

            # data = request.POST()
            # print(data)
            return redirect("homepage")
            # return render(request, "jobapp/home.html", {"msg":"Form Submitted"})
        else:
            return render(request, "jobapp/home.html", {"form":form, "msg":"Form Invalid"})

def save_applications(request):
    if request.method == 'GET':
        form = ApplicationModelForm()
        return render(request, 'jobapp/home.html', {'form':form})

    if request.method == 'POST':
        print(request.POST)
        form = ApplicationModelForm(request.POST) #calls a form related to model
        form.save() #saves data in database, works as create method
        #this is for manual entry 
        # apps = Application.objects.create(applicant_name=applicant_name, phone_no = phone_no, email= email, age=age)
        return render(request, "jobapp/home.html", {"msg":"Form Submitted"})
    
def delete(request,id):
    apps = Application.objects.get(id=id)
    print("apps id=====",apps)
    apps.delete()
    return redirect("homepage")

def edit(request,id):
    apps = Application.objects.get(id=id)
    if request.method == 'POST':
        form = ApplicationModelForm(request.POST, instance=apps)
        if form.is_valid():
            form.save()
        return redirect("homepage")
    else:
        form = ApplicationModelForm(instance=apps)
        return render(request, "jobapp/app_edit.html", {'form':form})
    
def retrieve(request, id):
    apps = Application.objects.get(id=id)
    form = ApplicationModelForm(instance=apps)
    return render(request, "jobapp/read.html", {'form':form})
