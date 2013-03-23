from django.db import models

class ClothManager(models.Manager):
    pass

class AccessoryManager(models.Manager):
    pass

class Cloth(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    clothes = ClothManager()

    class Meta:
        verbose_name_plural = 'clothes'

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    accessories = AccessoryManager()

    class Meta:
        verbose_name_plural = 'accessories'
