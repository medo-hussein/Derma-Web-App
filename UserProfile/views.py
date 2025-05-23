import re
from django.contrib import messages
from django.shortcuts import render, redirect
from test0.models import User
from UserProfile.models import Address
from .forms import CreateUserForm
from storeapp.models import Cart
import uuid
from django.contrib.auth import authenticate, login, logout
from storeapp.forms import AddressForm
# from .forms import AddressForm

# Create your views here.

def signup(request):
    form =  CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account Created! You can Login')
            request.session['nonuser'] = str(uuid.uuid4())
            cart = Cart.objects.create(session_id = request.session['nonuser'], completed=False)
            return redirect('signin')
    print ('done'+str(form.errors))
    context = {'form': form}
    return render(request, 'UserProfile/signup.html', context)

def signin(request):
    
    cart = Cart.objects.get(session_id = request.session['nonuser'], completed=False)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        #user = authenticate(request, email=email, password=password)
        user = User.objects.get(e_mail=email)
        print(email,' ',password)
        print(user)
        if user.check_password(password):
            
            login(request, user)
            cart.owner = request.user.customer
            cart.save()
            print("juuu"*56)
            cart = Cart.objects.get(session_id = request.session['nonuser'], completed=False)
            cartitems = cart.items.all()
            context = {'cart':cart, 'cartitems': cartitems}
            return render(request, 'storeapp/cart.html', context)
           
        else:
            messages.info(request, 'Invalid credentials')
            
    
    print(cart.owner)
    context = {'cart':cart}
    return render(request, 'UserProfile/login.html', context)

def signout(request):
    logout(request)
    return redirect('index')

def changeAddress(request):
    customer = request.user.customer
    address = Address.objects.get(customer=customer)
    form = AddressForm(instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST,instance=address)
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.customer = customer
            new_address.save()
            return redirect('checkout')
    context = {'form':form}
    return render(request, 'UserProfile/updateaddress.html', context)
    