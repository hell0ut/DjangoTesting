from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from autos.models import Make,Auto


class MainView(LoginRequiredMixin,View):
    def get(self,request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()
        ctx = {'make-count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html',ctx)


class MakeView(LoginRequiredMixin,View) :
    def get(self, request):
        ml = Make.objects.all();
        ctx = { 'make_list': ml };
        return render(request, 'autos/make_list.html', ctx)


class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    success_url = reverse_lazy('autos:all')
    fields = '__all__'


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    success_url = reverse_lazy('autos:all')
    fields = '__all__'


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    success_url = reverse_lazy('autos:all')
    fields = '__all__'


class AutoCreate(LoginRequiredMixin,CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')