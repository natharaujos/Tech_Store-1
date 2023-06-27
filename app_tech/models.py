from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.TextField(max_length=255)
    location = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.TextField(max_length=255)
    description = models.TextField()
    price  = models.DecimalField(max_digits = 10,decimal_places = 2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name    

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.client.username} Customer request {self.id}"
    
class OrderItem(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(help_text="Quantidade do mesmo produto selecionado")
    price = models.DecimalField(max_digits=10, decimal_places=2, editable = False)

    def __str__(self):
        return f"Order from {self.Order.client.username}, product : {self.Product}, quantity : {self.quantity}, price: {self.price}"
    
    def clean(self):
        if self.quantity > self.Product.quantity:
                raise ValidationError(f"{self.Product.name} quantity exceeds available stock. Quantity in Stock : {self.Product.quantity}")
    
    def save(self, *args, **kwargs):
        self.price = self.Product.price * self.quantity
        super().save(*args, **kwargs)

    def price_display(self):
        return self.price
