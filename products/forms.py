from django import forms

from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'user',
            'id',
            'name',
            'code',
            'color',
            'size',
            'price',
            'image'
        ]

    def clean_content(self, *args, **kwargs):
        name = self.cleaned_data.get('Name')
        if len(name) > 240:
            raise forms.ValidationError("Name is too long")
        return name

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        name = data.get('Name', None)
        if name == "":
            name = None
        codes = data.get("Code", None)
        if name is None and codes is None:
            raise forms.ValidationError('Name or Code is required.')
        return super().clean(*args, **kwargs)