from django.conf import settings
from django.db import models


def upload_products_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class ProductsQuerySet(models.QuerySet):
    pass


class ProductsManager(models.Manager):
    def get_queryset(self):
        return ProductsQuerySet(self.model, using=self._db)


class Products(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.DO_NOTHING)
    id          = models.BigIntegerField(primary_key=True,  blank=True)
    name       = models.CharField(max_length=100, null=True, blank=True)
    code       = models.CharField(max_length=30, null=True, blank=True)
    color       = models.CharField(max_length=120, null=True, blank=True)
    size       = models.CharField(max_length=120, null=True, blank=True)
    price       = models.CharField(max_length=120, null=True, blank=True)
    image       = models.ImageField(upload_to=upload_products_image, null=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ProductsManager()

    def __str__(self):
        return str(self.name)[:50]

    class Meta:
        verbose_name = 'Products List'
        verbose_name_plural = 'Products List'





