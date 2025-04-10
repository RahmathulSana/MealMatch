from django.shortcuts import render, redirect,get_object_or_404
from .forms import FoodItemForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import FoodItem 
from order.models import OrderDetail

def is_seller(user):
    return user.is_authenticated and user.role == 'seller'  

@login_required
@user_passes_test(is_seller, login_url='users:login', redirect_field_name=None)
def welcome(request):
    return render(request,'food/welcome.html')

@login_required
@user_passes_test(is_seller, login_url='users:login', redirect_field_name=None)
def add_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.seller = request.user 
            food_item.save()
            return redirect('food:food_list')  
    else:
        form = FoodItemForm()
    
    return render(request, 'food/add_food_item.html', {'form': form})




@login_required
@user_passes_test(is_seller, login_url='users:login', redirect_field_name=None)
def food_list(request):
    food_items = FoodItem.objects.filter(seller=request.user)  
    return render(request, 'food/food_list.html', {'food_items': food_items})

@login_required
@user_passes_test(is_seller, login_url='users:login', redirect_field_name=None)
def food_detail(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id, seller=request.user)  
    return render(request, 'food/food_detail.html', {'food_item': food_item})
@login_required
@user_passes_test(is_seller, login_url='users:login', redirect_field_name=None)
def update_food(request, food_id): 
    food_item = get_object_or_404(FoodItem, id=food_id)
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('food:food_detail', food_item.id)  
    else:
        form = FoodItemForm(instance=food_item)

    return render(request, 'food/update_food.html', {'form': form, 'food_item': food_item}) 

@login_required
@user_passes_test(is_seller, login_url='users:login', redirect_field_name=None)
def delete_food(request, food_id):
    food = get_object_or_404(FoodItem, id=food_id)
    food.delete()
    return redirect('food:food_list')  


@login_required
@user_passes_test(is_seller) 
def sales(request):
    sales = OrderDetail.objects.filter(food_item__seller=request.user)

    return render(request, 'food/sales.html', {'sales': sales})




