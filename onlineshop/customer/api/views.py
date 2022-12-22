from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, render, redirect
from django.core.mail import send_mail
from django.contrib import messages

from customer.api.serializer import *


def create_customer_property_func(req):
    customer = Customer.objects.create(
        username=req.POST['username'],
        email=req.POST['email'],
        phone=req.POST['phone'],
    )
    customer.save()
    customer.set_password(req.POST['password'])
    customer.save()


@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        # print(request.POST)
        res = dict()
        if not len(request.POST['password']) > 8:
            if request.POST['password'] == request.POST['password2']:
                res['success'] = True
                res['link'] = '/customer/login'
                create_customer_property_func(request)
            else:
                res['success'] = False
        else:
            res['success'] = False
        return Response(res)


@api_view(['GET', 'POST'])
def customerlist(request):
    if request.method == 'GET':
        customer = get_list_or_404(Customer)
        serializer = CustomerSerializer(customer, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        customer = CustomerSerializer(data=request.data)
        if customer.is_valid():
            customer_instance = customer.save()
            customer_instance.set_password(customer.validated_data['password'])
            customer_instance.save()


@api_view(['GET', 'POST'])
def forgetpassword(request):
    if request.method == 'POST':
        res = dict()
        username = request.POST['username']
        try:
            customer = Customer.objects.get(username=username)
            if customer:
                his_email = customer.email
                new_password = Customer.objects.make_random_password(length=20)
                res['success'] = True
                res['link'] = '/customer/login'
                res['msg'] = f'Your new password sent to {his_email}. Please login with this'
                messages.success(request, res['msg'])
                customer.set_password(new_password)
                customer.save()
                send_mail('your new password',
                          f'your reset password is {new_password}',
                          'security@onlineshop.com',
                          [his_email],
                          fail_silently=False, )
            else:
                res['success'] = False
                res['link'] = 'customer/forgetpassword'
                res['msg'] = 'This username is not exist!'
                messages.error(request, res['msg'])
                return Response(res, status=status.HTTP_400_BAD_REQUEST)

        except:
            res['success'] = False
            res['link'] = 'customer/forgetpassword'
            res['msg'] = 'Something went wrong'
            messages.error(request, res['msg'])
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

        return Response(res)
    return redirect('customer:forgetpassword')
