from django.contrib import admin
from .models import ToDoList, item

admin.site.register(ToDoList)
admin.site.register(item)
# Register your models here.
