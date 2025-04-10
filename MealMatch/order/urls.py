app_name = "order"

from django.urls import path
from .views import browse_food, food_detail, checkout, process_payment, order_confirmation,my_orders,show_reviews,order_detail,add_review,cancel_order_view

urlpatterns = [
    path('browse/', browse_food, name='browse_food'),
    path('food/<int:food_id>/', food_detail, name='food_detail'),  
    path('checkout/<int:order_id>/', checkout, name='checkout'), 
    path('payment/<int:order_id>/', process_payment, name='process_payment'),  
    path('order-confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),  
    path('food/<int:food_id>/reviews/', show_reviews, name='show_reviews'),  
    path('my-orders/', my_orders, name='my_orders'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('food/<int:food_id>/add_review/', add_review, name='add_review'),
    path('cancel_order/<int:order_id>/', cancel_order_view, name='cancel_order'),




]








