from django.db import models
from django.shortcuts import reverse 

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    info = models.TextField(blank=True)
    price = models.FloatField()
    cats = models.ManyToManyField("Cathegory", blank=True, related_name="products")
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product_detail_url", kwargs={"pk": self.id})
    
    class Meta:
        ordering = ["-price"]


class Cathegory(models.Model):
    title = models.CharField(max_length= 50, db_index=True)

    def get_absolute_url(self):
        return reverse("cathegory_detail_url", kwargs={"pk": self.id})


    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=150)
    email= models.EmailField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
