from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages

from product.models import Animal


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'product/home.html', {'request': request})
        else:
            message = 'username or password is not correct!'
            messages.error(request, message)
            return redirect('customer:login')

    return render(request, 'product/home.html', {'request': request})
