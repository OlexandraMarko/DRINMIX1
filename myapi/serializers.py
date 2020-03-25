from rest_framework import serializers

from .models import Cocktail
from .models import CafeIngredient
from .models import Ingredient
from .models import Order
from .models import Cafe
from .models import CocktailIngredient


class CafeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cafe
        fields = ('name', 'address', 'email', 'phone_number', 'cocktail', 'ingredient')


class CafeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CafeIngredient
        fields = ('ingredient', 'quantity')


class CocktailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cocktail
        fields = ('name', 'ingredient', 'price', 'image', 'volume', 'alcohol', 'custom', 'time')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity_mu', 'price_per_unit')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('price', 'date', 'cocktails', 'user', 'cafe')


class CocktailIngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CocktailIngredient
        fields = ('ingredient', 'amount_of_ingredient')
