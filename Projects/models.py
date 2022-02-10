from django.db import models

# Create your models here.
class Projects_overview(models.Model):
    id = models.AutoField(primary_key=True)
    totalprojects = models.IntegerField(default=0)
    ongoingprojects = models.IntegerField(default=0)
    certificates = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default='')
    Keywords = models.CharField(max_length=50,default='')
    Description = models.CharField(max_length=200,default='')
    Picture = models.ImageField(upload_to='projects/',default='')
    Link = models.CharField(max_length=200,default='')
    Aboutme = models.CharField(max_length=500,default='')
    contact = models.CharField(max_length=15,default='')
    email = models.CharField(max_length=50,default='')
    def __str__(self):
        return self.id

class Projects_details(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    Keywords = models.CharField(max_length=50,default='')
    Description = models.CharField(max_length=200,default='')
    total_picture = models.IntegerField(default=0)
    Picture = models.ImageField(upload_to='projects/',default='')
    Link = models.CharField(max_length=200,default='')
    def __str__(self):
        return self.id