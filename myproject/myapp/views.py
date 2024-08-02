from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpRequest
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import patient,consultation

# Create your views here.
def index(request : HttpRequest):
    patients = patient.objects.all()
    consultations = consultation.objects.all().__len__()
    if request.method == 'POST':
        patients = [ i for i in patients if request.POST['rech'] in i.name]
    context = {
        'patients':patients,
        'number':patients.__len__(),
        'numconsultations':consultations
    }
    return render(request,'index.html',context)
def counter(request):
    text = request.POST['text']
    l = len(text.split())
    return render(request,'counter.html',{'amount':l})
def register(request):
    return render(request,'pages-register.html')
def detail(request):
    username = request.GET.get('patientname')
    xpatient = patient.objects.get(name=username)
    return render(request,'detail.html',{'patient':xpatient})
def addpatient(request):
    return render(request,'pages-register-patient.html')
def check(request):
    cancel = request.POST.get('cancel')
    if cancel == 'true':
        return redirect('index')
    patient(name=request.POST.get('patientname'),job=request.POST.get('patientjob'),contact=request.POST.get('patientcontact')).save()
    return redirect('index')
def profil(request):
    return render(request,'users-profile.html')


def profilpatient(request, patientid):
    p1 = get_object_or_404(patient, id=patientid)
    consultations = consultation.objects.filter(idpatient=p1)
    return render(request, 'patient-prof.html', {'patient': p1, 'consultations': consultations})

import datetime

def createcons(request):
    patient_id = request.POST.get('patientid')
    description = request.POST.get('description')
    datetime_str = request.POST.get('datetime')
    
    date = datetime.datetime.fromisoformat(datetime_str)
    # Créer la consultation
    consultation.objects.create(idpatient_id=patient_id, description=description, date=date)
    
    # Rediriger vers la vue de profil patient avec l'ID du patient
    return redirect('profilpatient', patientid=patient_id)


def delete(request):
    cons = get_object_or_404(consultation,id=request.POST.get('idcons'))
    p1 = cons.idpatient
    cons.delete()
    return redirect('profilpatient',p1.id)

def modify(request):
    p1 = get_object_or_404(patient,id=request.POST.get('patientid'))
    p1.name = request.POST.get('fullName')
    p1.job = request.POST.get('job')
    p1.contact = request.POST.get('contact')
    p1.save()
    return redirect('profilpatient',p1.id)

def deletepatient(request):
    p1 = get_object_or_404(patient,id=request.POST.get('patientid'))
    p1.delete()
    return redirect('index')

def conslist(request):
    liste = consultation.objects.all()
    if request.method =='POST':
        liste = [i for i in liste if request.POST['rech'] in i.idpatient.name]
    context = {
        'consliste':liste
    }
    return render(request,'consultationliste.html',context)

def pagescontact(request):
    return render(request,'pages-contact.html')
def login(request):
    return render(request,'pages-login.html')