
from django.contrib import admin
from django.urls import include,path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('login', views.login),

    path('product',views.product),
    path('register',views.register),
    path('order',views.order),
    path('feedback',views.feedback2),
    path('review',views.review),
    path('design',include('design.urls')),



]
