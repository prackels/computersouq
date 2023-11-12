from django.urls import path
from . import views

app_name= 'dashboard'
urlpatterns = [
    path('addproducts/laptop', views.add_laptop, name= 'addlaptop'),
]
