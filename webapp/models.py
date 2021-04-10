from django.db import models


# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%d-%m-%y/')
    created_date = models.DateTimeField(auto_now_add=True)
    redirect_url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.headline


class test(models.Model):
    name = models.CharField(max_length=11)

    def __str__(self):
        return self.name