"""orders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from backend.views import CategoryView, ShopView, ProductInfoView, BasketView, RegisterAccount, PartnerUpdate

urlpatterns = [
     path('admin/', admin.site.urls),
     path('create_account/', RegisterAccount .as_view()),
     path('shop/', ShopView.as_view()),
     path('category/', CategoryView.as_view()),
     path('product/', ProductInfoView .as_view()),
     path('basket/', BasketView.as_view()),
     path('partnerupdate/', PartnerUpdate.as_view()),
     # path('sensors/<pk>/', SensoridView.as_view()),
]