from django.db import models

# Create your models here.

class userdata(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class products(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_img = models.ImageField(upload_to ='prod_img/', default="test")

    def __str__(self):
        return self.product_name

class latest_products(models.Model):
    la_prod_name = models.CharField(max_length=100)
    la_prod_price = models.IntegerField()
    la_prod_image = models.ImageField(upload_to ='prod_img/', default="test")

    def __str__(self):
        return self.la_prod_name