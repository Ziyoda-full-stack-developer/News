from django.urls import path
from .views import category, contact, index, single, featureDetail


urlpatterns = [
    path('category/', category, name="category"),
    path('contact/', contact, name="contact"),
    path('index/', index, name="index"),
    path('single/', single, name="single"),
    path('<int:id>/', featureDetail, name='featureDetail')
]