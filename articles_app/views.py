from datetime import date
from django.shortcuts import render
from . import models


def Articles(request):
    articles = models.Articles.objects.all().order_by('date')
    art = articles
    return render(request, 'articles.html', {'art': art} )
 