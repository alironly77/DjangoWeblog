from datetime import date
from django.shortcuts import render
from . import models
from django.http import HttpResponse


def Articles(request):
    articles = models.Articles.objects.all().order_by('date')
    art = articles
    return render(request, 'articles.html', {'art': art})


def Articles_detail(request, slug):
    return HttpResponse(slug)
