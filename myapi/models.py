from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=60)
    quantity_mu = models.CharField(max_length=20)
    price_per_unit = models.FloatField(max_length=60)

    def __str__(self):
        return self.name


class CocktailIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount_of_ingredient = models.FloatField()

    def __str__(self):
        return "%s %s" % (self.ingredient, self.amount_of_ingredient)


class Cocktail(models.Model):
    name = models.CharField(max_length=60)
    ingredients = models.ManyToManyField(CocktailIngredient)
    price = models.FloatField(max_length=60)
    image = models.ImageField()
    volume = models.IntegerField()
    alcohol = models.BooleanField()
    custom = models.BooleanField()
    time = models.IntegerField()

    def __str__(self):
        return self.name


class CafeIngredient(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=40)

    def __str__(self):
        return "%s %s" % (self.ingredient, self.quantity)


class Cafe(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    emails = models.EmailField()
    phone_number = models.IntegerField()
    cocktail = models.ManyToManyField(Cocktail)
    ingredient = models.ManyToManyField(CafeIngredient)

    def __str__(self):
        return self.name


class Order(models.Model):
    price = models.FloatField(max_length=60)
    date = models.DateField(max_length=60)
    cocktails = models.ManyToManyField(Cocktail)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.price, self.date)



