from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

class Store(models.Model):
  title = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  received = models.IntegerField(default = 0, blank =True)
  issued = models.IntegerField(default = 0, blank =True)
  quantity = models.IntegerField(default = 0, blank =True)
  created_by = models.ForeignKey(User, on_delete= models.PROTECT)
  DisplayFields = ['title','created','received','issued','quantity','created_by','status']
  def __str__(self):
    return self.title

  
  def status(self):
    if self.quantity >= 10:
      status = "good"
      return status
    elif self.quantity > 5 and self.quantity <= 10:
      status = "bad"
      return status
    elif self.quantity > 0 and self.quantity <= 5:
      status = "Critical"
      return status
    else :
      status = "out of stock"
      return status
  

class Author(models.Model):
  firstName = models.CharField(max_length =50)
  lastName = models.CharField(max_length =50)
  email = models.EmailField()
  dob  = models.DateTimeField()

  def __str__(self):
    Author_name = self.firstName + " " + self.lastName
    return Author_name
  
class Book(models.Model):
  title = models.ForeignKey(Store, null=True, blank=True, on_delete = models.PROTECT)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  year_of_pub = models.IntegerField()
  Description = models.TextField()

  def __str__(self):
    return self.title.title
