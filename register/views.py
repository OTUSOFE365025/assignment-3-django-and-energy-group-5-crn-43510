from django.shortcuts import render
from .forms import ScanForm
from .models import Product

def scan_view(request):
    form = ScanForm(request.POST or None)
    product = None
    error = None
    if request.method == "POST" and form.is_valid():
        upc = form.cleaned_data["upc"].strip()
        try:
            product = Product.objects.get(upc=upc)
        except Product.DoesNotExist:
            error = f"No product found for UPC {upc}."
    return render(request, "register/scan.html", {"form": form, "product": product, "error": error})
