from django.db import models

from django.urls import  reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=230, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
   
    class Meta:
        ordering = ('name'),
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('produce_category', args=[self.slug])    

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=230, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    discription = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='category', null=True, blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    creation= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return self.name
    
