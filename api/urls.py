from django.contrib import admin
from . import views
from django.urls import path, include, re_path

urlpatterns = [
    re_path('^$', views.index, name='home'),
    re_path(r'detail/$', views.detail, name='detail_product'),
    # re_path(r'get-price/$', views.price_amount, name='price_product'),

    # when product request (id, amount, discount)
    re_path(r'get-product/$', views.get_product, name='get_product')
]