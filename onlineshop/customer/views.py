from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from customer.forms import EditProfileForm
from customer.models import Customer, Passport
from product.models import Animal


# just render the related page
def login(request):
    return render(request, 'customer/login.html', {'request': request})


# just render the related page
def signup(request):
    return render(request, 'customer/signup.html', {'request': request})


# just render the related page
def forgetpassword(request):
    return render(request, 'customer/forget_password.html', {'request': request})


@login_required
def profile(request):
    if request.method == 'GET':
        this_user = Customer.objects.get(id=request.user.id)
        phone = this_user.phone
        address = this_user.address
        # print(this_user, phone, address)
        return render(request, 'customer/profile.html', {
            'request': request,
            'phone': phone,
            'address': address,
        })
    if request.method == 'POST':
        pass


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('customer:profile')
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'customer/profile_edit.html', context)


def auth_logout(request):
    logout(request)
    return render(request, 'product/home.html', {'request': request})
