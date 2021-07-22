from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Commande(models.Model):
	creation_date = models.DateField(auto_now_add=True)
	product = models.CharField(max_length=250)
	productype = models.CharField(max_length=100, blank=True)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=100)
	completed = models.BooleanField(default= False)


class Products(models.Model):
		product = models.CharField(max_length=500)
		tag = models.CharField(max_length=50, default='Médicament')
		ppa = models.DecimalField(decimal_places=2, max_digits=8, default=0)
		marge = models.IntegerField(default=20)
		pu = models.DecimalField(decimal_places=2, max_digits=8, default=0)