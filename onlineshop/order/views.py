from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from customer.models import Customer
from order.models import Order, OrderItem
from product.models import Animal


def cart(request):
    if request.session.get('cart'):
        the_cart = request.session.get('cart')
        product_list = dict()

        for i in the_cart:
            product = Animal.objects.filter(id=i).first()
            product_list[product] = the_cart[i]

        context = {
            'products': product_list
        }
        return render(request, 'order/cart.html', context)

    return render(request, 'order/cart.html', {'request': request})


@csrf_exempt
def single_product(request):
    if request.method == 'POST':
        product_id = request.POST['id']
        selected_product = get_object_or_404(Animal, id=product_id)
        return render(request, 'product/single_product.html', {'request': request, 'product': selected_product})
    return render(request, 'product/single_product.html', {'request': request})


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        qty = request.POST.get('qty')
        if not request.session.get('cart'):
            request.session['cart'] = {
                product_id: qty
            }
        else:
            the_cart = request.session.get('cart')
            the_cart[product_id] = qty
            request.session.modified = True

        print(request.session.get('cart'))
        return redirect("order:cart")


def delete_from_cart(request, product_id):
    the_cart = request.session.get('cart')
    the_cart.pop(str(product_id))
    request.session.modified = True
    return redirect("order:cart")


def checkout(request):
    if request.user.is_authenticated:
        order_item_list = list()
        the_cart = request.session.get('cart')
        # animal = get_object_or_404(Animal, id=id)
        if the_cart:
            for product_id in the_cart:
                selected_product = Animal.objects.filter(pk=product_id).first()
                # animal.booked_by_who.add(request.user)
                order_item = OrderItem.objects.create(product=selected_product)
                order_item_list.append(order_item)

                selected_product.booked_by_who.add(request.user)

            customer = Customer.objects.get(id=request.user.id)
            print(customer)
            order = Order.objects.create(
                customer=customer,
            )

            order.order_item.add(*order_item_list)
            request.session.pop('cart')

            messages.success(request, 'Your request recorded successfully')
            return render(request, "order/checkout_done.html", {'request': request})

        else:
            messages.error(request, "You don't have any requests yet!")
            return render(request, "order/checkout_done.html", {'request': request})

    else:
        return render(request, "customer/login.html", {'request': request})
