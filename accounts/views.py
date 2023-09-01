from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def dashbord(request):
    return render(request, 'dashboard.html')

def userRegisterView(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'register.html', {'form': form})

def userLoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # session_key = get_create_session(request)
        # cart = Cart.objects.get(cart_id=session_key)
        # is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
        # if is_cart_item_exists:
        #     cart_item = CartItem.objects.filter(cart=cart)
        #     for item in cart_item:
        #         item.user = user
        #         item.save()
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'signin.html')

def userLogoutView(request):
    logout(request)
    return render(request, 'signin.html')

