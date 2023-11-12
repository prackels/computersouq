from django import forms
from category.models import Laptops



class AddLaptopsForm(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = '__all__'