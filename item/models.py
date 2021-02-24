from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(unique=True)
    class Meta:
        ordering=('-name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item:item_by_category', args=[self.slug,])

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='item/images/')

    class Meta:
        ordering=('-title',)

    def __str__(self):
        return self.title
