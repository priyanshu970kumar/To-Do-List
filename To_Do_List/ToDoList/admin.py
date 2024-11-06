from django.contrib import admin
from ToDoList.models import Note_data

# Register your models here.
class Note_admin(admin.ModelAdmin):
    list_display=()
    
admin.site.register(Note_data)