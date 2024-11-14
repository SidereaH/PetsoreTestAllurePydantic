#store
import requests
import json
# GET
def get_store_inventory():
    url = "https://petstore.swagger.io/v2/store/inventory"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
# POS
def place_order():
    url = "https://petstore.swagger.io/v2/store/order"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "id": 2,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2024-10-07T13:37:07.111Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()
# GET
def get_order(order_id):
    url = f"https://petstore.swagger.io/v2/store/order/{order_id}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()
# DELETE
def delete_order(order_id):
    url = f"https://petstore.swagger.io/v2/store/order/{order_id}"
    headers = {"accept": "application/json"}
    response = requests.delete(url, headers=headers)
    return response.json()
"""
print("Store inventory:", get_store_inventory())
print("Placed order:", place_order())
print("Get order with ID 7:", get_order(7))
print("Delete order with ID 7:", delete_order(7))
"""

