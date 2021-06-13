from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number = models.IntegerField()
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kargs):
        self.slug = slugify(self.name)
        super(Contact, self).save(*args, **kargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts:create')
