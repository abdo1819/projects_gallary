from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Project,Branch,Group
# Create your views here.
def hello(request):
    return HttpResponse("You're looking at hello .")

# http://127.0.0.1:8000/computer/forth
def projects(request, branch_name, group_name):
    project_branch = Branch.objects.get(name=branch_name) 
    project_group  = Group.objects.get(name=group_name, branch=project_branch)
    projects_list = Project.objects.filter(group=project_group)
    context={
        'projects_list':projects_list,
    }
    template = 'viewer_core/projects.html'
    return render(request, template, context)
                                

