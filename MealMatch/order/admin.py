from django.contrib import admin
from .models import Review,OrderDetail

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('food', 'user', 'rating', 'created_at')  # Display key review details
    search_fields = ('food__name', 'user__username', 'comment')  # Search food name, user, and comment
    list_filter = ('rating', 'created_at')  # Allow filtering by rating and creation date

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user__role='buyer')  # Only show buyers' reviews
    
admin.site.register(Review, ReviewAdmin)



@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ("user", "food_item", "quantity", "total_price", "payment_method", "payment_status","order_status","transaction_date")
    list_filter = ("payment_method", "payment_status")
    search_fields = ("user__username", "food_item__Item_name", "upi_id", "card_number","payment_method")
    ordering = ("-transaction_date",)

