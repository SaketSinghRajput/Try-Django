from django.shortcuts import render

from .forms import ProductForm


from .models import Products
# Create your views here.

def dynamic_lookup_view(request, my_id):
    obj = Products.objects.get(id=my_id)
    context = {
        'object': obj
        }
    return render(request, "products/product_detail.html", context)




















def product_create_view(request):
    
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form': form
        }
    
    return render(request, "products/product_create.html", context)



def product_detail_view(request):
    
    obj = Products.objects.get(id=1)
    context = {
        'object': obj
        }
    return render(request, "products/product_detail.html", context)
