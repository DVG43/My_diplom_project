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


from backend.views import PartnerUpdate, RegisterAccount, CategoryView, ShopView, ProductInfoView, \
    BasketView, ContactView, OrderView, PartnerState, PartnerOrders

# poka iskluchil  LoginAccount  ConfirmAccount  AccountDetails,
app_name = 'backend'
urlpatterns = [

     path('create/account/', RegisterAccount .as_view(), name='user-register'),  # Регистрация методом POST
     path('partner/update/', PartnerUpdate.as_view(), name='partner-update'),   # Oбновления прайса от поставщика POST
     path('partner_status/', PartnerState.as_view(), name='partner-state'),  # работы со статусом поставщика GET and POST
     path('partner_orders/', PartnerOrders.as_view(), name='partner-orders'),   #  получения заказов поставщиками GET
     path('shop/', ShopView.as_view(), name='shops'),  # для просмотра списка магазинов GET
     path('category/', CategoryView.as_view(), name='categories'),  #  для просмотра категорий
     path('product/', ProductInfoView .as_view(), name='product'),  # для поиска товаров GET
     path('basket/', BasketView.as_view(), name='basket'),  #   работа с корзиной пользователя GET POST PUT DEL
     path('order/', OrderView.as_view(), name='order'),   # получения и размешения заказов пользователями GET POST
     path('user/contact/', ContactView.as_view(), name='user-contact'),  # работа с контактами покупателей GET POST PUT DEL
     # path('sensors/<pk>/', SensoridView.as_view()),
]


