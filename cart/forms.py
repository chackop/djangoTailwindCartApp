from django import forms

from .models import CartItem


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ("title", "price")
        widgets = {
            "title": forms.TextInput(attrs={"class": "m-2 text-gray-900"}),
            "price": forms.NumberInput(attrs={"class": "m-2 text-gray-900"}),
        }
        labels = {"price": "Enter your price here"}
