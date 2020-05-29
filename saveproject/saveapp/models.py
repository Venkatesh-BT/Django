from django.db import models
class employee(models.Model):
	name = models.CharField( max_length=50)
	salary = models.IntegerField()
	email_id = models.CharField( max_length=50)

    
# Create your models here.
