from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from geopy.distance import geodesic

# Create your views here.

def homePage(response):
    return render(response,'main_app/homePage.html')
    


def consultancyPage(response):
    data = 3
    return render(response,'main_app/optionPage.html',{"data":data})

def hospitalsPage(request):
    if request.method == "POST":
      uname = request.POST.get('username')
      passwd = request.POST.get('password')

      user = authenticate(request,username=uname,password=passwd)
        
      if user is not None:
        login(request,user)
        return redirect('dashboard/%s' %uname)
      
      else:
        return redirect('hospitalsPage')

    return render(request, "main_app/hospitalsPage.html")

def registrationPage(response):
    if response.method == 'POST':
        uname = response.POST.get('username')
        passwd = response.POST.get('password')
        ucord1 = response.POST.get('cord1')
        ucord2 = response.POST.get('cord2')
        total_beds = response.POST.get('total_beds')
        free_beds = response.POST.get('free_beds')

        new_user = User.objects.create_user(username=uname,password=passwd)
        new_user.save()

        hos = Hospital(name=uname,total_beds=total_beds,ucord1=ucord1,ucord2=ucord2,free_beds=free_beds)
        hos.save()

        return redirect('hospitalsPage')
    
    
    return render(response,'main_app/registrationPage.html')

@login_required(login_url='hospitalsPage')
def dashboard(response,name):
   if response.method == "POST":
        hos = Hospital.objects.filter(name=name)
        ucord1 = response.POST.get('cord1')
        ucord2 = response.POST.get('cord2')

        if ucord1 != None:
           hos.update(ucord1=ucord1)
        
        if ucord2 != None:
           hos.update(ucord2=ucord2)
           
           
   return render(response,'main_app/dashboardPage.html')

def logoutPage(response):
   logout(response)
   return redirect('hospitalsPage')

def EmergencyPage(response):
    if response.method == 'POST':
        ucord1 = response.POST.get('cord1')
        ucord2 = response.POST.get('cord2')


        ls = []
        hospital = {}

        location1 = (ucord1,ucord2)

        for i in Hospital.objects.all():
           
            location2 = (i.ucord1,i.ucord2)
            distance = round(geodesic(location1,location2).km)
            if i.free_beds == 0:
               continue
            hospital[distance] = i

        keys = list(hospital.keys())
        keys.sort()

        for i in keys:
           ls.append(hospital[i])
        
        data = zip(ls,keys)
        return render(response,'main_app/optionPage.html',{"data":data})
    
    return render(response,'main_app/emergencyPage.html')

def consultancyPage(response):
    doc = []
    for i in Doctor.objects.all():
       doc.append(i)
    
    data = doc
       

    return render(response,'main_app/consultancyPage.html',{"data":data})
