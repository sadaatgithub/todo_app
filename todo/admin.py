from django.contrib import admin
from .models import Task


admin.site.index_title = 'ToDo App'
admin.site.site_header = 'ToDo_App'
admin.site.site_title = 'ToDo_App'

# Register your models here.
admin.site.register(Task)