from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from datetime import datetime
import pika
from .forms import *
from django.contrib import messages

def home(request): 
    search = request.GET.get('search')
    
    if search:
        
        products = Product.objects.filter(name__icontains=search)
    
    else :
        products_list =  Product.objects.all()
        paginator = Paginator(products_list, 4)
        page = request.GET.get('page')
        products = paginator.get_page(page)

    return render(request, 'home.html', {'products':products})

def product(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product/product.html', {'product': product})

def create_order(request):
    if request.method == 'POST':
        client = request.user
        date = datetime.now()
        order = Order.objects.create(client=client, date=date)
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = Product.objects.get(pk=product_id)
        
        if quantity > product.quantity:
            # Quantidade solicitada é maior do que a quantidade em estoque
            error_message = f"Quantidade solicitada ({quantity}) excede a quantidade em estoque ({product.quantity})."
            return render(request, 'product/product.html', {'error_message': error_message})
        
        # Cria o item do pedido
        order_item = OrderItem.objects.create(Order=order, Product=product, quantity=quantity, price=quantity*product.price)
        
        # Atualiza a quantidade em estoque do produto
        product.quantity -= quantity
        product.save()
        messages.success(request, "Request created successfully!")
        
        return redirect('order-list')
    else:
        return render(request, 'create_order.html')

def order_list(request):
    orders = Order.objects.filter(client=request.user)
    return render(request, 'order_list.html', {'orders': orders})



