from django.db import models


#makemigrations - create changes and store in a file
#migrate - apply the pending changes created by makemigrations
# Create your models here.

class Contact(models.Model):
   name= models.CharField(max_length=100)
   email= models.EmailField(max_length=254)
   desc= models.TextField(200)
   date= models.DateField()

   def __str__(self):
      return self.name
      
class feedback(models.Model):
   name= models.CharField(max_length=100)
   desc= models.TextField(max_length=500)
   date= models.DateField()

   
   def __str__(self):
      return self.name
