from django.db import models
from django.utils import timezone

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class NewsModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, parent_link=True)
    title = models.CharField(max_length=255, verbose_name='Sarlavhasi')
    slug = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/news ')
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateField(auto_now_add=True)




