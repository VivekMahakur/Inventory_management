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
    result = None
    error = None
    
    if request.method == "POST":
        calculation_type = request.POST.get("calculation_type")
        try:
            price_per_kg = float(request.POST.get("price_per_kg", 0))

            if calculation_type == "find_quantity":
                total_price = float(request.POST.get("total_price", 0))
                if price_per_kg > 0:
                    quantity = total_price / price_per_kg
                    result = f"{quantity:.2f} Kg"
                else:
                    error = "Price per kg must be greater than zero."

            elif calculation_type == "find_price":
                quantity_kg = float(request.POST.get("quantity_kg", 0))
                price = quantity_kg * price_per_kg
                result = f"Rs. {price:.2f}"

        except ValueError:
            error = "Invalid input. Please enter valid numbers."

    return render(request, "calculator.html", {"result": result, "error": error})


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
    product.delete()  # Delete the product
    return redirect('inventory')  # Redirect to inventory after deletion
