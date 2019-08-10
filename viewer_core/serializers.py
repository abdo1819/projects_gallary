from rest_framework import serializers
from .models import Branch, Instractor, Student
from .models import Tag, Group, Project

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = ['name']

class InstractorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instractor
        fields = ['name', 'e_mail', 'img']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'e_mail', 'group', 'img']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'branch']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'img', 'description', 'markdown', 
                  'parent', 'group', 'tags', 
                  'students', 'instractors']
