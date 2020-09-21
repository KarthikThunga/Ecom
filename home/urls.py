from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index),
    path('product/<int:id>', views.product, name="product"),
    path('contact/', views.contact, name="contact"),
    path('allcat/', views.allcat),
    path('createprod/', views.createprod),
    path('catprod/<int:id>', views.catprod),
    path('updateprod/<int:id>', views.updateprod),
    path('deleteprod/<int:id>', views.deleteprod),
]