
from django.shortcuts import redirect, render

# Create your views here.
from .models import Patient,Doctor

from .forms import PatientForm,DoctorForm

def home(request):
    return render(request,'home.html')


def ViewAllPatients(request):
    all_users=Patient.objects.all()
    return render(request,'patient/view_all_users.html',{'data':all_users})

def patientregister(request):
    patientform=PatientForm()
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mobile=request.POST.get('phoneno')
        age=request.POST.get('age')
        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        Patient.objects.create(name=name,email=email,password=password,mobile_number=mobile,age=age,country=country,state=state,city=city)

        return redirect('ulogin')
    return render(request,'patient/patient_regiser.html')

def userlogin(request):
    obj=None
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            obj=Patient.objects.get(email=email,password=password)
            return redirect('uviewprofile',obj.id)
        except:
            pass
    return render(request,'patient/patient_login.html')

def editprofie(request,pk):
    id=Patient.objects.get(user_id=pk)
    form=PatientForm(instance=id)
    if request.method=='POST':
        forms=PatientForm(request.POST,instance=id)
        if forms.is_valid():
            forms.save()
            return redirect('uviewprofile',pk)
    return render(request,'patient/edituser.html',{'forms':form})


def viewprofile(request,pk):
    id=Patient.objects.get(user_id=pk)
    return render(request,'patient/view_user_profile.html',{'i':id})





# doctors 


def doctorlogin(request):
    obj=None
    if request.method=='POST':
        email=request.POST.get('demail')
        password=request.POST.get('dpassword')

        try:
            obj=Doctor.objects.get(demail=email,dpassword=password)
            print(obj.doctor_id)
            return redirect('dviewprofile',obj.doctor_id)
        except:
            print('no')
            pass
    return render(request,'doctors/doctorlogin.html')



def doctorviewprofile(request,pk):
    id=Doctor.objects.get(doctor_id=pk)
    print(id)
    return render(request,'doctors/doctorprofile.html',{'i':id})

def doctorregister(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        mobile=request.POST.get('phoneno')
        age=request.POST.get('age')
        special=request.POST.get('special')
        experience=request.POST.get('experience')

        country=request.POST.get('country')
        state=request.POST.get('state')
        city=request.POST.get('city')
        Doctor.objects.create(dname=name,demail=email,dpassword=password,dmobile_number=mobile,dage=age,dspecial=special,dexperience=experience,dcountry=country,dstate=state,dcity=city)

        return redirect('dlogin')
    return render(request,'doctors/doctorsignup.html')


def doc_edit(request,pk):
    id=Doctor.objects.get(doctor_id=pk)
    form=DoctorForm(instance=id)
    if request.method=='POST':
        form=DoctorForm(request.POST,instance=id)
        if form.is_valid():
            form.save()
            return redirect('dviewprofile',pk)
    return render(request,'doctors/editdoctor.html',{'forms':form})