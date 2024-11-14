import requests
BASE_URL = 'https://petstore.swagger.io/v2/user'
def create_user(user_data):
    response = requests.post(
        f'{BASE_URL}/createWithList',
        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
        json=[user_data]
    )
    return response.json()
def get_user(username):
    response = requests.get(
        f'{BASE_URL}/{username}',
        headers={'accept': 'application/json'}
    )
    return response.json()
def update_user(username, user_data):
    response = requests.put(
        f'{BASE_URL}/{username}',
        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
        json=user_data
    )
    return response.json()
def delete_user(username):
    response = requests.delete(
        f'{BASE_URL}/{username}',
        headers={'accept': 'application/json'}
    )
    return response.status_code  
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
"""
print("Creating user...")
print(create_user(user_data))
print("Getting user...")
print(get_user("user1"))
user_data["firstName"] = "UpdatedFirst"
print("Updating user...")
print(update_user("user1", user_data))

print("Deleting user...")
print(delete_user("user1"))"""
