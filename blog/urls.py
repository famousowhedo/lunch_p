from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.home, name='produce_category'),
    path('product/', views.about, name='home'),
]
