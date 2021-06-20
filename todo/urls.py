from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete,CustomLoginView
from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import reverse_lazy

urlpatterns = [
    path('',TaskList.as_view(), name='task'),
    path('detail/<int:pk>/',TaskDetail.as_view(), name='task_detail'),
    path('create-task/',TaskCreate.as_view(), name='task_create'),
    path('update-task/<int:pk>/',TaskUpdate.as_view(), name='task_update'),
    path('delete-task/<int:pk>/',TaskDelete.as_view(), name='task_delete'),
    path('login/',CustomLoginView.as_view(), name='login'),
    # path('login/',LoginView.as_view(template_name='todo/login.html',success_url = reverse_lazy('task')), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
]
