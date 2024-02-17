from django.shortcuts import render,redirect
from Accounts.models import User
from .models import Book,Cart


# Function for display all the items
def Booklist(request):
    if 's_name' in request.session:
        usr_id = request.session['s_name']
        usr_dtl = User.objects.filter(email=usr_id)
        book = Book.objects.all()
        return render(request,'booklist.html',{'books': book})
    else:
        return render(request, 'login.html')





# function for shows the details of the book
def BookDetails(request,id):
    if 's_name' in request.session:
        print("hi")
        print(request.session['s_name'])
        book_description = Book.objects.filter(id=id)
        print(book_description)
        return render(request, 'bookdetail.html',{'book_descriptions': book_description})
    else:
        return render(request, 'login.html')
# functions for shows the cart items
def Mycart(request):
    if's_name' in request.session:
        users_id = request.session['s_name']
        cart_object = Cart()
        cart_object.user = User.objects.get(email=users_id)
        x = cart_object.user
        total_price = 0
        cart_items = Cart.objects.filter(user_id=x)
        for i in cart_items:
            total_price = total_price +int(i.items.price)
        print(cart_items)
        return render(request,'mycart.html',{'cart_item':cart_items,'total_amount':total_price})
    else:
        return render(request, 'login.html')
# function for add the items to cart
def Addcart(request,id):
    if 's_name' in request.session:
        users_id = request.session['s_name']
        cart_object = Cart()
        cart_object.user = User.objects.get(email=users_id)
        print(cart_object.user)
        cart_object.items = Book.objects.get(id=id)
        print(cart_object.items)
        cart_object.save()
        x=cart_object.user
        print(x)
        total_price = 0
        cart_items = Cart.objects.filter(user_id=x)
        for i in cart_items:
            total_price = total_price +int(i.items.price)
        return render(request, 'mycart.html',{'cart_item':cart_items,'total_amount':total_price})
    else:
        return render(request, 'login.html')



# function for removes items from cart
def Removecart(request,id):
    cart_item_delete = Cart.objects.filter(id=id)
    cart_item_delete.delete()
    return redirect("/book/show_cart")


def Checkout(request,id):
    if 's_name' in request.session:
        user_id = request.session['s_name']
        cart_object = Cart()
        cart_object.user = User.objects.get(email=user_id)
        print(cart_object.user)
        cart_object.items = Book.objects.get(id=id)
        print(cart_object.items)
        cart_object.save()
        book_details = Book.objects.filter(id=id)
    return render(request, 'checkout.html',{'items':book_details})


def Order(request):
    return render(request, 'orders.html')

#  function for show the user profile
def Profile(request):
    if 's_name' in request.session:
        users_id = request.session['s_name']
        user_data = User.objects.filter(email=users_id)
    return render(request,'my_profile.html',{'myprofile':user_data})

# function for update/create/edit the profile
def Edit_profile(request):
    print("hi editing")
    if's_name' in request.session:
        print("session exists")
        users_id = request.session['s_name']
        user_data = User.objects.filter(email=users_id)
        for user_details in user_data:
            id = user_details.id
        if request.method == 'POST':
            print(user_data.values())
            print(id)
            user_detail = User.objects.get(email=users_id)
            print(request.POST.get('username'),request.POST.get('email'),request.POST.get('phone'),request.POST.get('bio'))
            user_detail.user_name = request.POST.get('username')
            user_detail.email = request.POST.get('email')
            user_detail.phone = request.POST.get('phone')
            user_detail.profile_pic = request.FILES.get('profilepic')
            user_detail.bio = request.POST.get('bio')
            user_detail.delivery_address = request.POST.get('address')
            user_detail.save()
            return redirect('/book/profile')
        return render(request,'create_profile.html',{'user_data':user_data})
    else:
        return render(request, 'login.html')


