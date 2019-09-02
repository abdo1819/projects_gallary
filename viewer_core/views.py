from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from rest_framework import viewsets

from .models import *
from .serializers import *


class BranchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Branchs to be viewed or edited.
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class InstractorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Instractors to be viewed or edited.
    """
    queryset = Instractor.objects.all()
    serializer_class = InstractorSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Students to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MainProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(parent__isnull=True)
    serializer_class = listProjectSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return listProjectSerializer
        if self.action == 'retrieve':
            return ProjectSerializer
        return ProjectSerializer # I dont' know what you want for create/destroy/update.    

    
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
