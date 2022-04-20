from django.contrib import admin
from main.models import List, Task
# Register your models here.

admin.site.register(List)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'list__name', 'created', 'due', 'owner', 'mark')
    list_filter = ('owner', 'list__name', 'mark')
    search_fields = ('name', 'owner')
    ordering = ('id',)
