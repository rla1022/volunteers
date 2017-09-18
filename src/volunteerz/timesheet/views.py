from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
# Create your views here.
#function based view
from .forms import TaskCreateForm
from .models import Task

# 

class TaskListView(ListView):
    def get_queryset(self):
        slug=self.kwargs.get("slug")
        if slug:
                queryset=Task.objects.filter(
                    Q(OpportunityNumber__iexact=slug)
                    )
        else:
            queryset=Task.objects.all()
        return queryset


class TaskDetailView(DetailView):
    queryset=Task.objects.all()

class TaskCreateView(LoginRequiredMixin,CreateView):
    template_name = 'task/addform.html'
    login_url='/login/'
    form_class = TaskCreateForm
   

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(TaskCreateView, self).form_valid(form)



        

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





