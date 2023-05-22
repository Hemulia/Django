from django.db import models

class Customer(models.Model):
	first_name= models.CharField(max_length=100)
	last_name= models.CharField(max_length=100)
	email= models.EmailField(unique=True)
	phone_number= models.CharField(max_length=20)
	address = models.TextField()
	
