from django import forms
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "category"]

    def clean_name(self):
        name = strip_tags(self.cleaned_data.get('name', ''))
        if not name.strip():
            raise forms.ValidationError('This field cannot be blank.')
        return name

    def clean_description(self):
        description = strip_tags(self.cleaned_data.get('description', ''))
        if not description.strip():
            raise forms.ValidationError('This field cannot be blank.')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if not price:
            raise forms.ValidationError('This field cannot be blank.')
        return price

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if not stock:
            raise forms.ValidationError('This field cannot be blank.')
        return stock

    def clean_category(self):
        category = strip_tags(self.cleaned_data.get('category', ''))
        if not category.strip():
            raise forms.ValidationError('This field cannot be blank.')
        return category