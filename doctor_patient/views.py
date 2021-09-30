from django.shortcuts import render, redirect
from .models import Doctor, Patient, Admin
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import PatientRegistration
from django.utils.decorators import decorator_from_middleware
from .middleware import PatientAuthMiddleware, AdminAuthMiddleware, AdminLoginMiddleware, PatientLoginMiddleware

# Create your views here.
@decorator_from_middleware(PatientLoginMiddleware)
def index(request):
    return render(request, 'index.html')

@decorator_from_middleware(PatientAuthMiddleware)
def home(request):
    return render(request, 'home.html')


@decorator_from_middleware(AdminAuthMiddleware)
def dashboard(request):
    doctors = Doctor.objects.all()
    return render(request, 'dashboard.html', {'doctors':doctors, 'Male':'Male', 'Female':'Female'})

def view(request, id):
    pass

def add(request):
    Doctor.objects.create(name=request.POST.get("name"), dob=request.POST.get("dob"), gender=request.POST.get("gender"), email=request.POST.get("email"), mobile=request.POST.get("mobile"),
                          state=request.POST.get("state"), city=request.POST.get("city"), nationality=request.POST.get("nationality"), zipcode=request.POST.get("zipcode"), 
                          bio=request.POST.get("bio"), imcid=request.POST.get("imcid"), regno=request.POST.get("regno"), specialization=request.POST.get("specialization"), shift=request.POST.get("shift"), 
                          degree=request.POST.get("degree"), online_profile_link=request.POST.get("online_profile_link"), yoe=request.POST.get("yoe"), language=request.POST.get("language"),
                          available=request.POST.get("available"), fees=request.POST.get("fees"))
    return redirect('dashboard')

def delete(request, id):
    Doctor.objects.filter(id=id).delete()
    return redirect('dashboard')

def update(request, id):
    Doctor.objects.filter(id=id).update(name=request.POST.get("name"), dob=request.POST.get("dob"), gender=request.POST.get("gender"), email=request.POST.get("email"), mobile=request.POST.get("mobile"),
                          state=request.POST.get("state"), city=request.POST.get("city"), nationality=request.POST.get("nationality"), zipcode=request.POST.get("zipcode"), 
                          bio=request.POST.get("bio"), imcid=request.POST.get("imcid"), regno=request.POST.get("regno"), specialization=request.POST.get("specialization"), shift=request.POST.get("shift"), 
                          degree=request.POST.get("degree"), online_profile_link=request.POST.get("online_profile_link"), yoe=request.POST.get("yoe"), language=request.POST.get("language"),
                          available=request.POST.get("available"), fees=request.POST.get("fees"))
    return redirect('dashboard')



def patientRegistration(request):
    email=request.POST.get('email')
    userid=request.POST.get('userid')
    password=request.POST.get('password')
    patient = Patient.objects.create(email=email, userid=userid, password=password)
    return redirect('index')
    
    
def patientLogin(request):
    if request.method=='POST':
        userid=request.POST.get('userid')
        password=request.POST.get('password')
        # patient = authenticate(username=userid, password=password)
        patient = Patient.objects.filter(userid=userid, password=password)
    
        #patient = authenticate(username=userid, password=password)
        if patient:
            print('If condition failed')
            request.session['userid']=userid
            return redirect('home')
        else:
            print("Failed")
            return redirect('index')
    
    
def logout(request):
    del request.session['userid']
    return redirect('index')

@decorator_from_middleware(AdminLoginMiddleware)
def adminLogin(request):
    return render(request, 'adminLogin.html')


def aLogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        # patient = authenticate(username=userid, password=password)
        admin = Admin.objects.filter(email=email, password=password)
        
        #patient = authenticate(username=userid, password=password)
        if admin:
            request.session['admin']=email
            return redirect('dashboard')
        else:
            return redirect('adminLogin')
        
def aLogout(request):
    del request.session['admin']
    return redirect('index')

@decorator_from_middleware(PatientAuthMiddleware)
def specialization(request, spec):
    doctors = Doctor.objects.filter(specialization=spec)
    return render(request, 'spec.html', {'doctors':doctors})