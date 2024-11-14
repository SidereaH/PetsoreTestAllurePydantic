import allure
from user_test import create_user, get_user, update_user, delete_user
from store_test import get_store_inventory, place_order, get_order, delete_order
@allure.step("Get store inventory")
def test_get_store_inventory():
    inventory = get_store_inventory()
    assert inventory is not None

@allure.step("Place order")

def test_place_order():
    order_data = {
        "id": 2,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2024-10-07T13:37:07.111Z",
        "status": "placed",
        "complete": True
    }
    order = OrderModel(**order_data)
    response = place_order(order.dict())
    assert response["id"] == order.id


@allure.step("Get order")
def test_get_order():
    order = get_order(7)
    assert order["id"] == 7

@allure.step("Delete order")
def test_delete_order():
    response = delete_order(7)
    assert response["code"] == 200

@allure.step("Create user")
def test_create_user():
    user_data = {
        "id": 0,
        "username": "user1",
        "firstName": "First",
        "lastName": "Last",
        "email": "user1@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 0
    }
    user = UserModel(**user_data)
    response = create_user([user.dict()])
    assert response[0]["username"] == user.username

@allure.step("Get user")
def test_get_user():
    username = "user1"
    user = get_user(username)
    assert user["username"] == username

@allure.step("Update user")
def test_update_user():
    username = "user1"
    updated_data = {
        "firstName": "UpdatedFirst",
        "lastName": "UpdatedLast",
        "email": "updated@example.com"
    }
    response = update_user(username, updated_data)
    assert response["firstName"] == "UpdatedFirst"
    assert response["lastName"] == "UpdatedLast"
    assert response["email"] == "updated@example.com"

@allure.step("Delete user")
def test_delete_user():
    username = "user1"
    status_code = delete_user(username)
    assert status_code == 200
