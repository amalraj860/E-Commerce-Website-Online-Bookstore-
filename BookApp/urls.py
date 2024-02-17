from django.urls import path
from . import views

urlpatterns = [

    path('booklist/', views.Booklist, name='book_list'),
    path('bookdetails/<int:id>',views.BookDetails, name='bookdetails'),
    path('addcart/<int:id>',views.Addcart, name='cart_details'),
    path('remove_cart/<int:id>',views.Removecart, name='remove_item'),
    path('show_cart/',views.Mycart,name='show_carts'),
    path('checkout/<int:id>',views.Checkout, name='checkout_detail'),
    path('orders/', views.Order, name='order_details'),
    path('profile/',views.Profile,name='profile'),
    path('edit_profile/',views.Edit_profile, name='edit_profile')


]
