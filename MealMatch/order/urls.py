app_name = "order"

from django.urls import path
from .views import browse_food, food_detail, checkout, process_payment, order_confirmation,my_orders,show_reviews,order_detail,add_review,cancel_order_view

urlpatterns = [
    path('browse/', browse_food, name='browse_food'),
    path('food/<int:food_id>/', food_detail, name='food_detail'),  # View and select food
    path('checkout/<int:order_id>/', checkout, name='checkout'),  # Checkout page
    path('payment/<int:order_id>/', process_payment, name='process_payment'),  # Process payment
    path('order-confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),  # Confirmation page
    path('food/<int:food_id>/reviews/', show_reviews, name='show_reviews'),  # View reviews
    path('my-orders/', my_orders, name='my_orders'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('food/<int:food_id>/add_review/', add_review, name='add_review'),
    path('cancel_order/<int:order_id>/', cancel_order_view, name='cancel_order'),




]








# app_name = "order"
# from django.urls import path
# from . views import browse_food,food_detail,buy_food,order_confirmation,show_reviews,checkout,payment_method,process_payment,payment_success

# urlpatterns = [
#     path('browse/', browse_food, name='browse_food'),
#     path('food/<int:food_id>/', food_detail, name='food_detail'),  # New URL pattern
#     path('food/<int:food_id>/buy/', buy_food, name='buy_food'),
#     path('order-confirmation/', order_confirmation, name='order_confirmation'),
#     path('food/<int:food_id>/reviews/', show_reviews, name='show_reviews'),
#     path('checkout/<int:food_id>/<int:order_id>/', checkout, name='checkout'),
#     path('payment_method/<int:food_id>/',payment_method,name='payment_method'),
#     path('process_payment/<int:food_id>/',process_payment, name='process_payment'),
#     path('payment_success/<int:food_id>/',payment_success, name='payment_success'),



# ]