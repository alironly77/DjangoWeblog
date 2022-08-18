from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'articles_app'
urlpatterns = [
    path('', views.Articles,name="Home"),
    path('<slug>', views.Articles_detail, name="detail"),
]

urlpatterns += staticfiles_urlpatterns()
