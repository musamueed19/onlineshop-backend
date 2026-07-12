from django.db import models

# Create your models here.
# Create Timestamp model
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    
    class Meta:
        abstract = True
        

class Category(TimestampModel):
    category_name = models.CharField(max_length=150)
    description = models.TextField()
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.category_name
    

    
class Product(TimestampModel):
    product_name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.product_name

 
class Order(TimestampModel):
    customer_name = models.CharField(max_length=150)
    customer_email = models.EmailField()
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order #{self.id}"

