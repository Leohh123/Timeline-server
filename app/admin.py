from django.contrib import admin

from .models import Stage, Task, Plan, Record

admin.site.register(Stage)
admin.site.register(Task)
admin.site.register(Plan)
admin.site.register(Record)
