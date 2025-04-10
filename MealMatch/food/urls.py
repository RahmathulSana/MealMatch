app_name = 'food'
from django.urls import path
from .views import add_food_item,food_detail,food_list,update_food, delete_food,sales,welcome



urlpatterns = [
    path('add-food/', add_food_item, name='add_food_item'),
    # path('dashboard/', seller_dashboard, name='seller_dashboard'),
    path('list/',food_list,name='food_list'),
    path('<int:food_id>/', food_detail, name='food_detail'),  # URL for individual food item details
    path('update/<int:food_id>/', update_food, name='update_food'),
    path('delete/<int:food_id>/', delete_food, name='delete_food'),
    path('sales/', sales, name='sales'),
    path('welcome/',welcome,name='welcome'),

    
]

