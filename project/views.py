from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core import serializers
from .models import UserData
from .forms import UserTest




# Create your views here.
def user_create(request):
    if request.method=='POST':
        form=UserTest(request.POST or None)
        if form.is_valid():
            form.save()

        return redirect('user_list')
    else:
        form=UserTest(request.GET)
    return render(request,'project/home.html',{'form':form})

def user_list(request):
    data=UserData.objects.all()
    return render(request,'project/list.html',{'data': data})



def user_update(request,id):
    user_data=UserData.objects.get(id=id)
    form=UserTest(request.POST or None, instance=user_data)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request,'project/list.html',{'form':form,'user_data':user_data})

def user_delete(request,id):
    user_data=UserData.objects.get(id=id)
    if request.method=="POST":
        user_data.delete()
        return redirect('user_list')
    return render(request,'project/delete.html',{'user_data':user_data})


""" 
def user_list_json(request):
    queryset= UserData.objects.all()
    queryset=serializers.serialize('json',queryset)
    return HttpResponse(queryset, content_type='application/json')

"""