from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="categories",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите стоимость продукта"
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения", auto_now=True
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец продукта",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]


class ContactInfo(models.Model):
    country = models.CharField("Страна", max_length=100)
    inn = models.CharField("ИНН", max_length=20)
    address = models.CharField("Адрес", max_length=255)

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактные информации"

    def __str__(self):
        return f"{self.country} - {self.address}"
