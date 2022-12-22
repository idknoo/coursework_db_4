from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from customer.models import Customer
from order.models import Order, OrderItem
from product.models import Product


def cart(request):
    if request.session.get('cart'):
        the_cart = request.session.get('cart')
        total = 0
        product_list = dict()

        for i in the_cart:
            product = Product.objects.filter(id=i).first()
            product_list[product] = the_cart[i]
            total += product.initial_price * int(the_cart[i])

        context = {
            'products': product_list,
            'total': total,
        }
        return render(request, 'order/cart.html', context)

    return render(request, 'order/cart.html', {'request': request})


@csrf_exempt
def single_product(request):
    if request.method == 'POST':
        product_id = request.POST['id']
        selected_product = get_object_or_404(Product, id=product_id)
        return render(request, 'product/single_product.html', {'request': request, 'product': selected_product})
    return render(request, 'product/single_product.html', {'request': request})


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        qty = request.POST['qty']
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
        total_price = 0
        the_cart = request.session.get('cart')  # {product_id: quantity, ...}

        if the_cart:
            for product_id in the_cart:
                selected_product = Product.objects.filter(pk=product_id).first()  # number of existing product in shop
                quantity = the_cart[product_id]  # number of product that user wants to buy

                if selected_product.stock >= int(quantity):
                    Product.objects.filter(pk=product_id).update(stock=selected_product.stock - int(quantity))

                order_item = OrderItem.objects.create(product=selected_product, quantity=quantity)
                order_item_list.append(order_item)
                total_price += selected_product.generate_final_price * int(quantity)  # calculate total price

            customer = Customer.objects.get(id=request.user.id)
            print(customer)
            order = Order.objects.create(
                customer=customer,
                total_price=total_price,
            )

            order.order_item.add(*order_item_list)
            request.session.pop('cart')

            messages.success(request, 'Your order Recorded successfully')
            return render(request, "order/checkout_done.html", {'request': request})

        else:
            messages.error(request, "you don't have any orders yet!")
            return render(request, "order/checkout_done.html", {'request': request})

    else:
        return render(request, "customer/login.html", {'request': request})
