from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreate
from django.http import HttpResponse

# Read
def index(request):
    inventory = Product.objects.all()
    return render(request, 'product/sarisari.html', {'inventory': inventory})

# Create
def upload(request):
    upload = ProductCreate()
    if request.method == "POST":
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('''Your form is wrong. Go back and try again.''')
    else:
        return render(request, 'product/upload_form.html', {'upload_form': upload})
    
# Update
def update(request, product_id):
    product_id = int(product_id)
    try: # try-catch
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist: # DoesNotExist is the exception that denotes the Product is not in the database
        return redirect('index')
    product_form = ProductCreate(request.POST or None, instance=product)
    if product_form.is_valid():
        product_form.save() # Save changes made to the selected Product
        return redirect('index')
    return render(request, 'product/upload_form.html', {'upload_form': product_form})
    
# Delete
def delete(request, product_id):
    product_id = int(product_id)
    try: # try-catch
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist: # DoesNotExist is the exception that denotes the Product is not in the database
        return redirect('index')
    product.delete()
    return redirect('index')