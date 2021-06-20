
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

#---------  classbased views   -------

class TaskList(LoginRequiredMixin,ListView):     #show only title
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin,DetailView):   #show details of specific title
    model = Task
    context_object_name = 'task'
    # template_name = 'folder/appname'  #we can changes html name as per our will

class TaskCreate(LoginRequiredMixin,CreateView):#for edit of specific title
    model = Task
    fields = "__all__"
    # fields = ['create','desc']  # edit only specific fields only
    success_url = reverse_lazy('task')

class TaskUpdate(LoginRequiredMixin,UpdateView):#update specific task
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    success_url = reverse_lazy('task')

class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task')