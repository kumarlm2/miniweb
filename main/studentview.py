from django.shortcuts import render,get_object_or_404
from .models import Class,User,MeetUrl,Timings
from .forms import MeetUrlModelForm,CustomUserCreationForm,JoinClassForm

from django.http import JsonResponse,HttpResponseRedirect
from django.views.generic import CreateView,UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

import json



@csrf_exempt
def AddClass(request):
    if request.method == 'POST':
        form = JoinClassForm(data=request.POST,user=request.user)
        if form.is_valid():
            print("valid")
            return HttpResponseRedirect('/profile')
        return render(request, 'main/create.html',{'form':form})
    form = JoinClassForm(user=request.user)
    return render(request, 'main/create.html',{'form':form})  

@csrf_exempt
def DeleteView(request,classname):
    if request.method == 'DELETE':
        classname = Class.objects.get(classname=classname)
        classname.user.remove(request.user)
        classname.save()
        return JsonResponse({'success':'deleted successfully'},safe=True,status = 201)
    return JsonResponse({'error':'not allowed'},safe=False,status = 200)   



class ClassJoinView(LoginRequiredMixin,UpdateView):
    model = Class
    login_url = '/accounts/login/'
    fields = '__all__'
    template_name = 'main/create.html'
    success_url = '/profile_student'
    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())    
