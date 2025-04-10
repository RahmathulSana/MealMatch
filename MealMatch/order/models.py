from django.db import models
from django.conf import settings
from food.models import FoodItem  # Import FoodItem from the food app
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils.timezone import now



class Review(models.Model):
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.food.Item_name} ({self.rating}★)"
    


ORDER_STATUS = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
    ('canceled', 'Canceled'),
]

class OrderDetail(models.Model):
    PAYMENT_METHODS = [
        ('UPI', 'UPI Payment'),
        ('Card', 'Credit/Debit Card'),
        ('COP', 'Cash on Pickup'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Buyer
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)  # Ordered food
    quantity = models.PositiveIntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    payment_status = models.BooleanField(default=False)  # True if successful
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS, default="pending")  # Track order status
    upi_id = models.CharField(max_length=50, blank=True, null=True)  # Store if UPI
    card_number = models.CharField(max_length=16, blank=True, null=True)  # Store if Card
    transaction_date = models.DateTimeField(auto_now_add=True)
     
    def can_cancel(self):
     return now() - self.transaction_date <= timedelta(hours=1)
    
    def cancel_order(self):
     """Cancels the order if within 1 hour"""
     if self.can_cancel():
        self.order_status = 'canceled'
        self.save()
        return True
     return False

    def __str__(self):
        return f"{self.user.username} - {self.food_item.Item_name} - {self.order_status} - {self.payment_method}"

    
# class Payment(models.Model):
#     PAYMENT_METHODS = [
#         ('UPI', 'UPI Payment'),
#         ('Card', 'Credit/Debit Card'),
#         ('COP', 'Cash on Pickup'),
#     ]

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Buyer
#     food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)  # Ordered food
#     quantity = models.PositiveIntegerField()
#     price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
#     payment_status = models.BooleanField(default=False)  # True if successful
#     upi_id = models.CharField(max_length=50, blank=True, null=True)  # Store if UPI
#     card_number = models.CharField(max_length=16, blank=True, null=True)  # Store if Card
#     transaction_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.food_item.name} - {self.payment_method}"
    




