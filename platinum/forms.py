from django.forms import ModelForm
from .models import *


class CartModelForm(ModelForm):
    class Meta:
        model = Cart
        fields = ["oil", "amount"]