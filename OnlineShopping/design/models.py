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
    Customer_name = models.CharField(max_length=250, default="")
    Email= models.CharField(max_length=250, default="")
    Password = models.CharField(max_length=250, default="")
    Phone_no= models.CharField(max_length=250, default="")


class Product(models.Model):
   # Customer=models.ForeignKey(Customer,on_delete='CASCADE')
   # Category = models.ForeignKey(category,on_delete='CASCADE')
   # Supplier = models.ForeignKey(Supplier, on_delete='CASCADE')
    product_Id = models.CharField(max_length=200,default="")
    Product_name = models.CharField(max_length=250, default="")
    description = models.CharField(max_length=250, default="")
    Stock = models.IntegerField(default=20000)
    Price = models.IntegerField( default=1)






class Payment(models.Model):
    #Customer = models.ForeignKey(Customer, on_delete='CASCADE')
    product_code=models.CharField(max_length=250, default="")
    quantity = models.CharField(max_length=250, default="")
    Price = models.CharField(max_length=250, default="")
    total= models.CharField(max_length=250, default="")




class feedback(models.Model):
    c_Name = models.CharField(max_length=250, default="")
    email = models.CharField(max_length=250, default="")
    message = models.CharField(max_length=250, default="")
