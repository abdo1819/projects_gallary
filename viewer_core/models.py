from django.db import models



class Branch(models.Model):
    name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name


class Instractor(models.Model):
    name = models.CharField(max_length=200)
    e_mait = models.EmailField()
    img = models.ImageField(null=True,upload_to="img/instractor/", blank=True)

    def __str__(self):
        return self.name




class Student(models.Model):
    name = models.CharField(max_length=200)
    e_mait = models.EmailField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    img = models.ImageField(null=True,upload_to="img/student/", blank=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(null=True, upload_to="img/project/")
    description = models.TextField()
    markdown = models.TextField()
    branch = models.ManyToManyField('Branch')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField('Tag')
    students = models.ManyToManyField('Student')
    instractors = models.ManyToManyField('Instractor')

    def __str__(self):
        return self.title
    
    def has_parent(self):
        if self.parent is None:
            return False
        return True
