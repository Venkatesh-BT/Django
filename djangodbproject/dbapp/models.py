from django.db import models
class student(models.Model):
    # TODO: Define fields here
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    branch=models.CharField(max_length=20)
    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        def __str__(self):
        	return self.name


    
   
    # TODO: Define custom methods here

    

# Create your models here.