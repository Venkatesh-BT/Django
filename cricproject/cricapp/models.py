from django.db import models
class player(models.Model):
	name = models.CharField( max_length=50)
	jersy_num = models.IntegerField()
	address = models.CharField( max_length=50)
	department = models.CharField( max_length=50)
	class Meta:
		verbose_name = "player"
		verbose_name_plural = "players"
	def __str__(self):
		return self.name
        


# Create your models here.
