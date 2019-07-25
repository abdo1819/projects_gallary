from django.db import models



class Branch(models.Model):
    name = models.CharField(max_length=200)


class Instractor(models.Model):
    name = models.CharField(max_length=200)
    e_mait = models.EmailField()
    img = models.ImageField(null=True,upload_to="img/instractor/")
    project = models.ManyToManyField('Project')



class Student(models.Model):
    name = models.CharField(max_length=200)
    e_mait = models.EmailField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    img = models.ImageField(null=True,upload_to="img/student/")
    project = models.ManyToManyField('Project')
    


class Tag(models.Model):
    name = models.CharField(max_length=200)
    project = models.ManyToManyField('Project')



class Project(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(null=True, upload_to="img/project/")
    description = models.TextField()
    markdown = models.TextField()
    branch = models.ManyToManyField('Branch')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    
