import pytest
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from rest_framework.authtoken.models import Token
from backend.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken, User

# FIXTURES ***************************************************************************************

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    # фикстура создания пользователя
    def make_user(**kwargs):
        kwargs['password'] = test_password
        kwargs['email'] = 'santuk@mail.ru'
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user

@pytest.fixture
def get_or_create_token(db, create_user):
    # фикстура создания токена пока не используется
    user = create_user()
    token, _ = Token.objects.get_or_create(user=user)
    #print(token)
    return token


@pytest.fixture
def api_client_with_credentials(db, create_user, client):
    # фикстура автоматической авторизации без токена - используется она
    user = create_user()
    client.force_authenticate(user=user)
    yield client
    client.force_authenticate(user=None)


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


# TESTS GET ********************************************************************************************************
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('user@mail.ru', '1624')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_unauthorized_request(client):
    response = client.get('user/login/')
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_shop(client, shop_factory):


# Arrange
    shop = shop_factory(_quantity=2)

# Act
    response = client.get('/API/V1/shop/')

# Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_category(client, category_factory):


# Arrange
    category = category_factory(_quantity=2)

# Act
    response = client.get('/API/V1/categories/')

# Assert
    assert response.status_code == 200





@pytest.mark.django_db
def test_get_product(client, shop_factory, category_factory, product_factory, product_info_factory):

# Arrange

# Act
    response = client.get('/API/V1/product/')

# Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_order(client, create_user, order_factory, contact_factory, api_client_with_credentials):

# Arrange

# Act
    response = api_client_with_credentials.get('/API/V1/order/')

# Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_contact(client, create_user, api_client_with_credentials, contact_factory):
    # закоментил код с аутентификацией  которая не работает в таком виде
    # token = get_or_create_token()
    # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    response = api_client_with_credentials.get('/API/V1/user/contact/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_basket(client, create_user, api_client_with_credentials, order_factory,
                    order_item_factory, product_factory, product_info_factory,
                    parameter_factory, product_parameter_factory):

    response = api_client_with_credentials.get('/API/V1/basket/')

    assert response.status_code == 200


# TESTS POST ********************************************************************************************************



@pytest.mark.django_db
def test_chenge_product_in_bascet(client, create_user, api_client_with_credentials, product_info_factory, order_factory,
                                  order_item_factory):

    response = api_client_with_credentials.post('/API/V1/basket/', data={"product_info": 2, "quantity": 8})

    assert response.status_code == 200
