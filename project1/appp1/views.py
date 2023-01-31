from django.shortcuts import render
from .forms import BoxDetailsForm
from .models import BoxDetails
from django.http import HttpResponseRedirect
from django.contrib import messages
from .filters import BoxDetailsFilter
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here

def homepage(request):
    return HttpResponseRedirect('/')

def add_new_student(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            bx=BoxDetailsForm(request.POST)
            if bx.is_valid():
                name=bx.cleaned_data.get('name')
                qbox_no=bx.cleaned_data.get('qbox_no')
                email=bx.cleaned_data.get('email')
                password=bx.cleaned_data.get('password')
                sudo_password=bx.cleaned_data.get('sudo_password')
                source=bx.cleaned_data.get('source')
                teleport=bx.cleaned_data.get('teleport')
                apihub=bx.cleaned_data.get('apihub')
                web_frontend=bx.cleaned_data.get('web_frontend')
                checkpoints=bx.cleaned_data.get('checkpoints')
                cxr_api=bx.cleaned_data.get('cxr_api')
                dcmio=bx.cleaned_data.get('dcmio')
                additional=bx.cleaned_data.get('additional')
                reg= BoxDetails(name=name, email=email,password=password,source=source,teleport=teleport,additional=additional,dcmio=dcmio,
                apihub=apihub,web_frontend=web_frontend,checkpoints=checkpoints,cxr_api=cxr_api,qbox_no=qbox_no,sudo_password=sudo_password)
                reg.save()
                messages.success(request,"DATA IS UPDATED")
                return HttpResponseRedirect('/')
        else:
            bx= BoxDetailsForm()
            dt= BoxDetails.objects.all()
            myFilter=BoxDetailsFilter(request.GET,queryset=dt)
            dt=myFilter.qs
    

            return render(request,'home.html',{'box':bx,'details':dt,'myFilter':myFilter})
    else:
        return HttpResponseRedirect('/login/')


def delete_data(request, id):
    
    if request.method=="POST":
        todo=BoxDetails.objects.get(pk=id)
        return render(request, 'delete.html', {'todo':todo})

def confirmed_delete(request, id):
    if request.method=="POST":
        dt=BoxDetails.objects.get(pk=id)
        dt.delete()
        return HttpResponseRedirect('/')



def update_details(request, id):
    if request.method=='POST':
        dt= BoxDetails.objects.get(pk=id)
        fm=BoxDetailsForm(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
            messages.success(request,'DATA IS UPDATED')
    else:
        dt= BoxDetails.objects.get(pk=id)
        fm=BoxDetailsForm(instance=dt)
    return render(request, 'updatedetails.html', {'form':fm})


def search_data(request):
    if request.method=="GET":
        query=request.GET.get('query',None)
        if query:
            data= BoxDetails.objects.filter(name__icontains=query)
        else:
            data = "No Data"
        return render(request,'home.html',{'data':data})

        

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            lg = AuthenticationForm(request=request, data=request.POST)
            if lg.is_valid():
                username=lg.cleaned_data.get('username')
                password=lg.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
        else:
            lg= AuthenticationForm()
        return render(request, 'login.html', {'form':lg})
    else:
        return HttpResponseRedirect('/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
