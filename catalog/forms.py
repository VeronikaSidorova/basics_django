import os

from PIL import Image
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)


class StyleFormMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


FORBIDDEN_WORDS = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар'
        ]


def _validate_forbidden_words(text):
    text_lower = text.lower()
    for word in FORBIDDEN_WORDS:
        if word in text_lower:
            raise forms.ValidationError(
                f"Использование слова '{word}' запрещено."
            )


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', )

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        _validate_forbidden_words(name)
        return name


    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        _validate_forbidden_words(description)
        return description


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError("Цена не может быть пустой.")
        if price <= 0:
            raise forms.ValidationError("Цена не может быть нулевой или отрицательной.")
        return price


    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            return image  # поле необязательно или уже проверено

        # Проверка размера файла (в байтах)
        max_size = 5 * 1024 * 1024  # 5 МБ
        if image.size > max_size:
            raise ValidationError("Размер файла не должен превышать 5 МБ.")

        # Проверка формата изображения
        try:
            # image.file — это файловый объект, читаемый библиотекой PIL
            img = Image.open(image.file)
            img_format = img.format.lower()
            if img_format not in ['jpeg', 'png']:
                raise ValidationError("Допустимые форматы изображений: JPEG, PNG.")
        except Exception:
            raise ValidationError("Загруженный файл не является допустимым изображением.")
        return image

