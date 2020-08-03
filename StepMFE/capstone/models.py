from django.db import models

class Business(models.Model):
  uid = models.AutoField(primary_key = True, unique = True)
  name = models.CharField(max_length = 64)
  link = models.URLField(max_length = 64)
  category = models.CharField(max_length = 32)
  description = models.TextField()
  email = models.EmailField(max_length = 64)
  contact_name = models.CharField(max_length = 64)
  address = models.CharField(max_length = 64, blank = True)
  zipcode = models.CharField(max_length = 12, blank = True)
  state = models.CharField(max_length = 64, blank = True)
  country = models.CharField(max_length = 64, blank = True)

  class Meta:
    managed = True

  def __str__(self): 
    return self.name 

class Search(models.Model):
  category = models.CharField(max_length = 32, blank = True)
  keywords = models.CharField(max_length = 32, blank = True)

  class Meta:
    managed = True

  def __str__(self): 
    return self.name 