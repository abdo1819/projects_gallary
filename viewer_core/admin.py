from django.contrib import admin

# Register your models here.
from .models import Student,Branch,Instractor,Project,Tag,Group

admin.site.register(Student)
admin.site.register(Branch)
admin.site.register(Instractor)
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Group)
