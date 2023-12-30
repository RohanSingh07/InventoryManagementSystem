from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=100)
    price = models.FloatField()
    # Discount
    discount_price = models.FloatField()
    # Brand
    Brand = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField(blank=True, null=True)
    # Images of the products
    image1 = models.ImageField(blank=True, null=True, upload_to='Products/')
    # color
    color = models.CharField(max_length=50, blank=True, null=True)
    # Date Added
    date = models.DateField(auto_now_add=True)
    # size chart
    def __str__(self):
        return self.Name
    # Fields for seller
    SellerName = models.TextField()
    Stock = models.IntegerField(default=1)

    @property
    def image1_url(self):
        if self.image1 and hasattr(self.image1, 'url'):
            return self.image1.url


    def get_abs_url(self):
        return reverse(viewname="Base:product-page",
                       kwargs={
                           'slug': self.slug
                       })
