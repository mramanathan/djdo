from django.contrib import admin

# Register your models here.

from .models import Todo
## Above can be written like this too:
#from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'is_completed', 'due_date')
	list_filter  = ('is_completed',)

admin.site.register(Todo, TodoAdmin)
