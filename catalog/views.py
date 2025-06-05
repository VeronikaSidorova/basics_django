from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product, ContactInfo


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Выводим последние 5 продуктов в консоль
    print("Последние 5 созданных продуктов:")
    for product in latest_products:
        print(f"ID: {product.id}, Название: {product.name}, Создано: {product.created_at}")

    context = {
        'latest_products': latest_products,
    }
    return render(request, "home.html", context)


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
