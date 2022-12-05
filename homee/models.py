from django.db import models

# Create your models here.

class detail(models.Model):
	FOOD_TYPE = (
		('CST/19/IFT/00405','CST/19/IFT/00405'),
		('CST/19/IFT/00408','CST/19/IFT/00408'),
		('CST/19/SWE/00403','CST/19/SWE/00403'),
		('CST/19/IFT/00404','CST/19/IFT/00404'),
		('CST/19/IFT/00403','CST/19/IFT/00403'),
		('CST/19/IFT/00412','CST/19/IFT/00412'),
	)
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	PhoneNumber = models.CharField(max_length=11)
	Reg_No = models.CharField(max_length=30, choices = FOOD_TYPE)
	StreetAddress = models.CharField(max_length=50)
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)


	def __str__(self):
		return self.FirstName