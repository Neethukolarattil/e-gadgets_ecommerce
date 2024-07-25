from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class products(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="product_images",null=True)
    options=(
        ("smart phone","smart phone"),
        ("tablets","tablets"),
        ("smart watch","smart watch"),
        ("Laptop","Laptop")
    )
    category=models.CharField(max_length=100,choices=options)
    def __str__(self):
        return self.title

class Cart(models.Model):
    products=models.ForeignKey(products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    status=models.CharField(max_length=100,default="added")

    @property
    def total_price(self):
        tamount=self.products.price*self.quantity
        return tamount
    
class Orders(models.Model):
    products=models.ForeignKey(products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    options=(
        ("order placed","order placed"),
        ("shipped","shipped"),
        ("Out for Delivery","Out for Delivery"),
        ("Delivered","Delivered")
    )
    status=models.CharField(max_length=100,default="order placed",choices=options)