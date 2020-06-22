from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    itemsJson = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    totalPrice = models.CharField(max_length=50,default="")
    zipcode = models.CharField(max_length=12)
    cHolder = models.CharField(max_length=70,default="")
    cardNo = models.CharField(max_length=25,default="")
    expDate= models.CharField(max_length=12,default="")
    cvv = models.CharField(max_length=5,default="")

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Order " + str(self.update_id)
