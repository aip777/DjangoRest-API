from rest_framework import serializers

from products.models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields =[
            'user',
            'id',
            'name',
            'code',
            'color',
            'size',
            'price',
            'image'
        ]


    def validate(self, data):
        name = data.get("name", None)
        if name == "":
            name = None
        code = data.get("Code", None)
        if name is None and code is None:
            raise serializers.ValidationError("Name or Code is required.")
        return data

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields =[

            'price',

        ]

class ColorSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields =[

            'color',
            'size',

        ]

class ProductsAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields =[
            'id',
            'name',
            'code',
        ]




