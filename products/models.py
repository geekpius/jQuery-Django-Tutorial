from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 150)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
