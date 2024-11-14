from django.db import models


class Make(models.Model):
    name = models.CharField(max_length=32, unique=True)
    logo = models.ImageField(upload_to='img/logos/', blank=True, null=True)
    count = models.IntegerField(default=0)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.name


class Model(models.Model):
    make = models.ForeignKey(Make, related_name='models', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    count = models.IntegerField(default=0)
    url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Generation(models.Model):
    model = models.ForeignKey(Model, related_name='generations', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/generations/', blank=True, null=True)
    count = models.IntegerField(default=0)
    url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.name}"


# class Listing(models.Model):
#     generation = models.ForeignKey(Generation, related_name='listings', on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     make = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     year = models.PositiveIntegerField()
#     mileage = models.IntegerField()
#     city = models.CharField(max_length=100)
#     modification = models.CharField(max_length=100, blank=True, null=True)
#     url = models.URLField(max_length=255)
#
#     def __str__(self):
#         return f"{self.make} {self.model} {self.year} in {self.city}"
