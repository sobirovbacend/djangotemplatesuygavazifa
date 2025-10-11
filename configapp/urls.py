from django.urls import path
from .views import *

urlpatterns = [
    path('category',category),
    path('product',product),
    path('ordetail',order_detail),
    path('order',orders),
    path('allpagemodel',allfuncmodel)
]