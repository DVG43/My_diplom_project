import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from backend.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken, User

# FIXTURES ***************************************************************************************

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_factory():
    def factory(*args, **kwargs):
        return baker.make(User, *args, **kwargs)

    return factory


@pytest.fixture
def contact_factory():
    def factory(*args, **kwargs):
        return baker.make(Contact, *args, **kwargs)

    return factory


@pytest.fixture
def shop_factory():
    def factory(*args, **kwargs):
        return baker.make(Shop, *args, **kwargs)

    return factory


@pytest.fixture
def category_factory():
    def factory(*args, **kwargs):
        return baker.make(Category, *args, **kwargs)

    return factory


@pytest.fixture
def product_factory():
    def factory(*args, **kwargs):
        return baker.make(Product, *args, **kwargs)

    return factory


@pytest.fixture
def product_info_factory():
    def factory(*args, **kwargs):
        return baker.make(ProductInfo, *args, **kwargs)

    return factory


@pytest.fixture
def parameter_factory():
    def factory(*args, **kwargs):
        return baker.make(Parameter, *args, **kwargs)

    return factory


@pytest.fixture
def product_parameter_factory():
    def factory(*args, **kwargs):
        return baker.make(ProductParameter, *args, **kwargs)

    return factory


@pytest.fixture
def order_factory():
    def factory(*args, **kwargs):
        return baker.make(Order, *args, **kwargs)

    return factory

@pytest.fixture
def order_item_factory():
    def factory(*args, **kwargs):
        return baker.make(OrderItem, *args, **kwargs)

    return factory


@pytest.fixture
def confirm_email_token_factory():
    def factory (*args, **kwargs):
        return baker.make(ConfirmEmailToken, *args, **kwargs)

    return factory


# TESTS ********************************************************************************************************


@pytest.mark.django_db
def test_get_shop(client, shop_factory):


# Arrange
    shop = shop_factory(_quantity=2)

# Act
    response = client.get('/API/V1/shop/')

# Assert
    assert response.status_code == 200
    # data = response.json()
    # print(data)
    # assert len(data) == len(shop)




@pytest.mark.django_db
def test_get_category(client, category_factory):


# Arrange
    category = category_factory(_quantity=2)

# Act
    response = client.get('/API/V1/categories/')

# Assert
    assert response.status_code == 200



# @pytest.mark.django_db
# def test_create_accaunt(client):
# #     count = Message.objects.count()
# #
#     response = client.post('/API/V1/user/register/', data={'first_name': 'dmitrii',
#                                                     'last_name':'galuta',
#                                                     'email': 'santuk@mail.ru',
#                                                     'password': 'hjgvmjgdfg1345',
#                                                     'company': 'jhgjhj',
#                                                     'position': 'jghhgv'})
#
#     assert response.status_code == 201


@pytest.mark.django_db
def test_get_product(client, shop_factory, category_factory, product_factory, product_info_factory):

# Arrange

# Act
    response = client.get('/API/V1/product/')

# Assert
    assert response.status_code == 200