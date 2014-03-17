from django.db import models

class User(models.Model):
#     UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=128, unique=True)
    Password = models.CharField(max_length=128)
    Email = models.EmailField()
    Telephone = models.CharField(max_length=10)
    Address = models.CharField(max_length=128)
    Type = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.Username
    
class Product(models.Model):
#     ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=128, unique=True)
    Description = models.CharField(max_length=128)
    PostDate = models.DateTimeField()
    SellingPrice = models.DecimalField(max_digits=8, decimal_places=2)
    StartingBid =  models.DecimalField(max_digits=8, decimal_places=2)
    EndDate = models.DateTimeField()
    ViewNo = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.ProductName
    
class Bid(models.Model):
#     BidID = models.AutoField(primary_key=True)
    User = models.ForeignKey(User)
    Product = models.ForeignKey(Product)
    BidNo = models.IntegerField(default=0)
    Time = models.DateTimeField()
    Quantity = models.IntegerField(default=0)
    Subtotal =  models.DecimalField(max_digits=8, decimal_places=2)
    
    def __unicode__(self):
        return self.BidID
    
class Comment(models.Model):
    User = models.ForeignKey(User)
    Product = models.ForeignKey(Product)
    Comment = models.CharField(max_length=128)
    
class Rating(models.Model):
    User = models.ForeignKey(User)
    Product = models.ForeignKey(Product)
    Rating = models.IntegerField(default=0)