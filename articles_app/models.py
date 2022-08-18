from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:60] + ' .....'
