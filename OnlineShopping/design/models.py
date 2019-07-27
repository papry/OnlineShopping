from django.db import models

class category(models.Model):
    Category_name=models.CharField(max_length=250,default="")

class Supplier(models.Model):
    Supplier_name = models.CharField(max_length=250, default="")
    Address = models.CharField(max_length=250, default="")
    Phone_no = models.CharField(max_length=250,default="")


class Admin(models.Model):
    Admin_name = models.CharField(max_length=250, default="")
    Password = models.CharField(max_length=250, default="")


class Customer(models.Model):
    Customer_name = models.CharField(max_length=250,null=True, blank=True, default="")
    Email= models.CharField(max_length=250,null=True, blank=True, default="")
    Password = models.CharField(max_length=250,null=True, blank=True, default="")
    Phone_no= models.CharField(max_length=250,null=True, blank=True, default="")


class Product(models.Model):

    product_Id = models.CharField(max_length=200,default="")
    Product_name = models.CharField(max_length=250, default="")
    description = models.CharField(max_length=250, default="")
    Stock =models.CharField(max_length=250, default="")
    Price = models.CharField(max_length=250, default="")






class Payment(models.Model):

    product_code=models.CharField(max_length=250,null=True, blank=True, default="")
    quantity = models.CharField(max_length=250,null=True, blank=True, default="")
    Price = models.CharField(max_length=250,null=True, blank=True, default="")
    total= models.CharField(max_length=250,null=True, blank=True, default="")




class feedback(models.Model):
    feedname = models.CharField(max_length=250, default="")
    email = models.CharField(max_length=250, default="")
    message = models.CharField(max_length=250, default="")
