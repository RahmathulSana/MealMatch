app_name = 'users'
from django.urls import path
from .views import register,create, user_login,home,user_logout,contact,about
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('create/',create,name = 'create'),
    path('login/', user_login, name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('seller/', seller_dashboard, name='seller_dashboard'),
    path('logout/', user_logout, name='logout'),  # New logout URL
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    

]