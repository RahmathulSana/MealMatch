from django.shortcuts import render, get_object_or_404, redirect
from food.models import FoodItem
from .models import Review, OrderDetail
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db import transaction
import time
from django.utils.timezone import now
from datetime import timedelta

def is_buyer(user):
    return user.role == 'buyer'

@login_required
@user_passes_test(is_buyer)
def buyer_dashboard(request):
    return render(request, 'users/browse_food.html')

@login_required
@user_passes_test(is_buyer)
def browse_food(request):
    query = request.GET.get('search')  # Get the search query from the user
    if query:
        food_items = FoodItem.objects.filter(Item_name__icontains=query)  # Filter based on food name
    else:
        food_items = FoodItem.objects.all()  # Show all food items if no search term is given

    return render(request, 'order/browse_food.html', {'food_items': food_items, 'query': query})

 



@login_required
@user_passes_test(is_buyer)
def food_detail(request, food_id):
    """View food details and create a pending order"""
    food = get_object_or_404(FoodItem, id=food_id)

    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))

        if food.quantity < quantity:
            messages.error(request, "Not enough stock available.")
            return redirect('order:food_detail', food_id=food.id)

        with transaction.atomic():
            food.quantity -= quantity
            food.save()

            # Create pending order
            order = OrderDetail.objects.create(
                user=request.user,
                food_item=food,
                quantity=quantity,
                price_per_item=food.price,
                total_price=food.price * quantity,
                payment_status=False,
                order_status="pending"
            )

        return redirect('order:checkout', order_id=order.id)

    return render(request, 'order/food_detail.html', {'food': food})

@login_required
def checkout(request, order_id):
    """Review order and choose payment method"""
    order = get_object_or_404(OrderDetail, id=order_id, user=request.user, order_status="pending")

    if request.method == "POST":
        payment_method = request.POST.get("payment_method")

        if payment_method not in dict(OrderDetail.PAYMENT_METHODS):
            messages.error(request, "Invalid payment method.")
            return redirect('order:checkout', order_id=order.id)

        # Save payment method before processing
        order.payment_method = payment_method
        order.save()

        return redirect('order:process_payment', order_id=order.id)

    return render(request, 'order/checkout.html', {'order': order})


@login_required
def process_payment(request, order_id):
    """Process payment and finalize order"""
    order = get_object_or_404(OrderDetail, id=order_id, user=request.user, order_status="pending")

    if request.method == "POST":
        payment_method = order.payment_method

        # Simulate payment success
        if payment_method in ["UPI", "Card"]:
            order.payment_status = True
            order.order_status = "paid"
        else:  
            order.payment_status = False
            order.order_status = "pending"

        order.save()

        return render(request, "order/payment_loading.html", {"order_id": order.id})  # ✅ Redirect to loading page

    return render(request, "order/payment.html", {"order": order})


@login_required
def order_confirmation(request, order_id):
    """Display order success message"""
    order = get_object_or_404(OrderDetail, id=order_id, user=request.user)
    return render(request, 'order/order_confirmation.html', {'order': order})


@login_required
def show_reviews(request, food_id):
    """Display all reviews for a food item"""
    food = get_object_or_404(FoodItem, id=food_id)
    reviews = food.reviews.all()
    return render(request, 'order/show_reviews.html', {'food': food, 'reviews': reviews})



    



@login_required
@user_passes_test(is_buyer)
def my_orders(request):
    orders = OrderDetail.objects.filter(user=request.user).order_by('-transaction_date')
    return render(request, 'order/my_orders.html', {'orders': orders})

@login_required
@user_passes_test(is_buyer)
def order_detail(request, order_id):
    order = get_object_or_404(OrderDetail, id=order_id)
    return render(request, 'order/order_detail.html', {'order': order})


@login_required
@user_passes_test(is_buyer)
def add_review(request, food_id):
    # ✅ Make sure the user has an order for this food item
    order = OrderDetail.objects.filter(food_item__id=food_id, user=request.user).first()

    if request.method == "POST":
        rating = int(request.POST.get("rating"))
        comment = request.POST.get("comment")

        if rating < 1 or rating > 5:
            messages.error(request, "Invalid rating. Please select a value between 1 and 5.")
            return redirect('order:order_detail', order_id=order.id)

        # ✅ Create a review for the correct FoodItem
        Review.objects.create(
            user=request.user,
            food=order.food_item,  # 🔥 Now linking to FoodItem, not OrderDetail
            rating=rating,
            comment=comment
        )

        return redirect('order:order_detail', order_id=order.id)

    return render(request, 'order/add_review.html', {'order': order})


def cancel_order_view(request, order_id):
    order = get_object_or_404(OrderDetail, id=order_id, user=request.user)

    if order.order_status == 'Cancelled':
        messages.warning(request, "Your order has already been canceled.")  # New message for already canceled orders
    elif hasattr(order, 'cancel_order'):  # Ensure cancel_order method exists
        order.cancel_order()
        messages.success(request, "Your order has been successfully canceled.")
    else:
        messages.error(request, "Order cancellation period has expired.")

    return redirect('order:my_orders')
# @login_required
# @user_passes_test(is_buyer)
# def add_review(request,order_id):
#     order = get_object_or_404(OrderDetail, id=order_id)

#     if request.method == "POST":
#         rating = int(request.POST.get("rating"))
#         comment = request.POST.get("comment")

#         if rating < 1 or rating > 5:
#             messages.error(request, "Invalid rating. Please select a value between 1 and 5.")
#             return redirect('order:order_detail', order_id=order.id)

#         Review.objects.create(
#             user=request.user,
#             food=order.food_item,
#             rating=rating,
#             comment= comment
#         )

#         messages.success(request, "Review submitted successfully!")
#         return redirect('order:my_orders')

#     return render(request, 'order/add_review.html', {'order': order})







