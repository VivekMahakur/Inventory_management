from django.shortcuts import render, redirect, get_object_or_404
from .models import Product  # Assuming you have a Product model

def homepage(request):
    return render(request, 'homepage.html')

def inventory(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'inventory.html', {'products': products})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        # Update product logic here
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.save()
        return redirect('inventory')  # Redirect to inventory after saving
    return render(request, 'edit_product.html', {'product': product})

def calculator(request):
    return render(request, 'calculator.html')

def add_product(request):
    if request.method == 'POST':
        # Add product logic here
        new_product = Product(
            name=request.POST['name'],
            category=request.POST['category'],
            price=request.POST['price'],
            stock=request.POST['stock']
        )
        new_product.save()
        return redirect('inventory')  # Redirect to inventory after adding
    return render(request, 'inventory.html')  # Show inventory if not POST

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('inventory')  # Redirect to inventory after deletion
