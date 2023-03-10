from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from customer.forms import EditProfileForm
from customer.models import Customer, Passport
from product.models import Animal

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

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

@login_required
def profile_edit_passport(request):
    if request.method == 'POST':
        form = EditProfileFormPassport(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('customer:profile')
    else:
        form = EditProfileFormPassport(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'customer/profile_edit_passport.html', context)


def auth_logout(request):
    logout(request)
    return render(request, 'product/home.html', {'request': request})



@ login_required
def booked_animals_list(request):
    new = Animal.newmanager.filter(booked_by_who=request.user)
    print(new)
    return render(request,
                  'customer/orderhistory.html',
                  {'new': new})


@ login_required
def booked_add(request, id):
    animal = get_object_or_404(Animal, id=id)
    # if animal.favourites.filter(id=request.user.id).exists():
    #     animal.favourites.remove(request.user)
    # else:
    animal.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])