from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView
# Create your views here.
#function based view
from .forms import HoursCreateForm, HoursLocationCreateForm
from .models import HoursLocation

# 

class HoursListView(ListView):
    def get_queryset(self):
        slug=self.kwargs.get("slug")
        if slug:
                queryset=HoursLocation.objects.filter(
                    Q(OpportunityNumber__iexact=slug)
                    )
        else:
            queryset=HoursLocation.objects.all()
        return queryset


class HoursDetailView(DetailView):
    queryset=HoursLocation.objects.all()

class HoursLocationCreateView(LoginRequiredMixin,CreateView):
    template_name = 'hours/addform.html'
    login_url='/login/'
    form_class = HoursLocationCreateForm
   

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(HoursLocationCreateView, self).form_valid(form)



        

        #@login_required(login_url='/login/')
# def HoursCreateView(request):
#     form = HoursLocationCreateForm(request.POST or None)
#     if form.is_valid():
#         if request.user.is_authenticated():
#             instance=form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#             return HttpResponseRedirect("/hours/")
#     if form.errors:
#         print(form.errors)

#     template_name ='hours/addform.html'
#     context = {"form": form}
#     return render(request, template_name, context)



# def HoursListView(request):
#     template_name ='hours/hourslist.html'
#     queryset = HoursLocation.objects.all()
#     context ={
#         "object_list": queryset
#     }
#     return render(request,template_name, context)





