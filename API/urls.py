from django.urls import path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('product/', views.product_list, name='product'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
