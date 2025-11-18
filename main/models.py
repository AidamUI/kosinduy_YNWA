# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def increase_stock(self, amount):
        self.stock += amount
        self.save()

    def decrease_stock(self, amount):
        if amount <= self.stock:
            self.stock -= amount
            self.save()
            return True
        return False
    
    def is_in_stock(self):
        return self.stock > 0
    

