from email.mime import image
from email.policy import default
from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', blank=True)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:60] + ' .....'
