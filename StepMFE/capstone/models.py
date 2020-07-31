from django.db import models

class Business(models.Model):
  uid = models.AutoField(primary_key = True, unique = True)
  name = models.CharField(max_length = 64)
  link = models.URLField(max_length = 64)
  description = models.TextField()
  email = models.EmailField(max_length = 64)
  contact_name = models.CharField(max_length = 64)
  address = models.CharField(max_length = 64)
  zipcode = models.CharField(max_length = 12)
  state = models.CharField(max_length = 64)
  country = models.CharField(max_length = 64)

  def __str__(self): 
    return self.name 