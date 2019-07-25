from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)


class Branch(models.Model):
    name = models.CharField(max_legth=200)


class Instractor(models.Model):
    name = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch on_delete=models.CASCADE)
    e_mait = models.EmailField()

class student(models.Model):
    name = models.CharField(max_length=200)
    e_mait = models.EmailField()
    branch = models.ForeignKey(Branch on_delete=models.CASCADE)


class year(models.Model):
    name = models.CharField(max_length=200)
