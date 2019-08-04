from django.db import models



class Branch(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Instractor(models.Model):
    name = models.CharField(max_length=200)
    e_mail = models.EmailField()
    img = models.ImageField(null=True,upload_to="img/instractor/", blank=True)

    def __str__(self):
        return self.name




class Student(models.Model):
    name = models.CharField(max_length=200)
    e_mail = models.EmailField()
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    img = models.ImageField(null=True,upload_to="img/student/", blank=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(null=True, upload_to="img/project/")
    description = models.TextField()
    markdown = models.TextField(null=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    group = models.ManyToManyField('Group')
    tags = models.ManyToManyField('Tag', null=True)
    students = models.ManyToManyField('Student')
    instractors = models.ManyToManyField('Instractor')

    def __str__(self):
        return self.title

    def has_parent(self):
        if self.parent is None:
            return False
        return True
