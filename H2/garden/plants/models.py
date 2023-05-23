from django.db import models

class Plant(models.Model):
   name = models.CharField(max_length=200)
   sown = models.DateTimeField(auto_now=True, null = True)
   
   def __str__(self):
       return self.name	
