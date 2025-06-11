from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from catalog.forms import ProductForm
from catalog.models import Product, ContactInfo


def home(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, "products_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, "product_detail.html", context)



def contacts(request):
    contact_info = ContactInfo.objects.first()
    return render(request, "contacts.html", {'contact_info': contact_info})


def contact(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
