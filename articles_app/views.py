from datetime import date
from django.shortcuts import render, redirect
from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms


def Articles(request):
    articles = models.Articles.objects.all().order_by('-date')
    art = articles
    return render(request, 'articles.html', {'art': art})


@login_required(login_url='accounts:login')
def Articles_detail(request, slug):
    article = models.Articles.objects.get(slug=slug)
    return render(request, 'articles_detail.html', {'article': article})


@login_required(login_url='accounts:login')
def Create(request):
    if request.method == 'POST':
        form = forms.CreateArticles(request.POST, request.FILES)
        if form.is_valid():
            inst= form.save(commit=False)
            inst.author = request.user
            inst.save()
            return redirect('articles_app:Home')
    else:
        form = forms.CreateArticles()
    return render(request, 'create.html', {'form': form})
