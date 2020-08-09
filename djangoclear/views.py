from django.shortcuts import render
from django.views import generic
import datetime

class TemplateView(generic.TemplateView):
    def get(self,request):
        return render(request,'home/main.html')