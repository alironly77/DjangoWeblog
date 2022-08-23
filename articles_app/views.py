from datetime import date
from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def Articles(request):
    articles = models.Articles.objects.all().order_by('-date')
    art = articles
    return render(request, 'articles.html', {'art': art})

@login_required(login_url='/accounts/login/')
def Articles_detail(request, slug):
    article = models.Articles.objects.get(slug=slug)
    return render(request, 'articles_detail.html', {'article': article})


@login_required(login_url='/accounts/login/')
def Create(request):
    return render(request, 'create.html')
