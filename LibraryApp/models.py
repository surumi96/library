from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    BookName=models.CharField(max_length=255)
    AuthorName=models.CharField(max_length=255)
    Number=models.IntegerField()
    def __str__(self):
        return self.BookName

class User(AbstractUser):
    studclass=models.IntegerField(null=True, blank=True)
    # Email=models.CharField(max_length=255,null=True, blank=True )
    fine=models.IntegerField(null=True, blank=True)


class Order(models.Model):
    BookName = models.ForeignKey(Book, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    issuedate = models.DateField(null=True,blank=True,auto_now_add=True)
    returndate = models.DateField(null=True,blank=True)
    fine = models.FloatField(null=True,blank=True)





