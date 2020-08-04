from django.shortcuts import render
from django.views import generic
import datetime

class TemplateView(generic.TemplateView):
    def get(self,request):
        context={
            'time':datetime.datetime.now()
        }
        return render(request,'home/index.html',context)