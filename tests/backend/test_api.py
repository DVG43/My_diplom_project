import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from backend.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken


@pytest.fixture
def client():
    return APIClient()


# @pytest.fixture
# def user():
#     return User.objects.create_user('admin')


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


@pytest.mark.django_db
def test_get_shop(client, shop_factory):
# Arrange
    shop = shop_factory(_quantity=5)

# Act
    response = client.get('/API/V1/shop/')

# Assert
    assert response.status_code == 200
#     data = response.json()
#     assert len(data) == len(messages)
#     for i, m in enumerate(data):
#         assert m['text'] == messages[i].text


@pytest.mark.django_db
def test_get_category(client, category_factory):
# Arrange
    category = category_factory(_quantity=2)

# Act
    response = client.get('/API/V1/categories/')

# Assert
    assert response.status_code == 200



# @pytest.mark.django_db
# def test_create_message(client, user):
#     count = Message.objects.count()
#
#     response = client.post('/messages/', data={'user': user.id, 'text': 'test text'})
#
#     assert response.status_code == 201
#     assert Message.objects.count() == count + 1