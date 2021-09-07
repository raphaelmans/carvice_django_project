from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('aboutus', views.AboutUsView.as_view(), name='about_us'),
]