from django.shortcuts import render
from .forms import EmployeeRegistration
from .models import UserProfile
from django.http import HttpResponseRedirect
# Create your views here.
def test(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = EmployeeRegistration() #added it because the form needs to clear up after submitting the entries
    else:
        fm = EmployeeRegistration()
    userData=UserProfile.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'userData':userData})

def delete(request,id):
    if request.method=='POST':
        userDelete=UserProfile.objects.get(pk=id)
        userDelete.delete()
    return HttpResponseRedirect('/enroll')

def update(request,id):
    if request.method == 'POST':
        userUpdate=UserProfile.objects.get(pk=id)
        fm=EmployeeRegistration(request.POST,instance=userUpdate)
        if fm.is_valid():
            fm.save()            
    else:
        userUpdate=UserProfile.objects.get(pk=id)
        fm=EmployeeRegistration(instance=userUpdate)
    return render(request,'enroll/update.html',{'form':fm})
        
        
        
    
        