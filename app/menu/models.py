from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='posts/default.jpg')
    video = models.FileField(upload_to='menu_videos', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    # class Meta:
    #     ordering = ['name']
    #     verbose_name = 'Menu'
    #     verb