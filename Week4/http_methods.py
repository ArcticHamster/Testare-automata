import requests

# ----------- Add User ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/users'
# body_json = {
#     "firstName": "Testare",
#     "lastName": "Automata",
#     "email": "pyta_2@itfactory.ro",
#     "password": "1234567"
# }
#
# response = requests.post(url, json=body_json)
#
# print(response.status_code)

# ----------- Add User ----------


# ----------- Login ----------
url = 'https://thinking-tester-contact-list.herokuapp.com/users/login'
body_json = {
    "email": "pyta_2@itfactory.ro",
    "password": "1234567"
}

response = requests.post(url, json=body_json)

response_json = response.json()

auth_token = response_json['token']

print(response_json['token'])
headers = {
    'Authorization': f'Bearer {auth_token}'
}

# ----------- Login ----------
# ----------- Add Contacts ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
# body_json = {
#     "firstName": "John",
#     "lastName": "Doe",
#     "birthdate": "1970-01-01",
#     "email": "jdoe@fake.com",
#     "phone": "8005555555",
#     "street1": "1 Main St.",
#     "street2": "Apartment A",
#     "city": "Anytown",
#     "stateProvince": "KS",
#     "postalCode": "12345",
#     "country": "USA"
# }
#
# response = requests.post(url, headers=headers, json=body_json)
#
# print(response.status_code)
# ----------- Add Contacts ----------
# ----------- Delete Contacts ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/64c7e0d4208731001381618d'
# response = requests.delete(url, headers=headers)
#
# print(response.status_code)

# ----------- Delete Contacts ----------
# ----------- Get Contact List ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
#
# response = requests.get(url, headers=headers)
#
# print(response.text)
# ----------- Get Contact List ----------
# ----------- Update Contact ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/64c7e1f12087310013816190'
# body_json = {
#     "firstName": "Marcel",
#     "lastName": "Miller",
#     "birthdate": "1992-02-02",
#     "email": "amiller@fake.com",
#     "phone": "8005554242",
#     "street1": "13 School St.",
#     "street2": "Apt. 5",
#     "city": "Washington",
#     "stateProvince": "QC",
#     "postalCode": "A1A1A1",
#     "country": "Canada"
# }
#
# response = requests.put(url, headers=headers, json=body_json)
#
# print(response.text)
# ----------- Update Contact ----------
# ----------- Update Contact ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/64c7e1f12087310013816190'
# body_json = {
#     "firstName": "Bianca"
# }
#
# response = requests.patch(url, headers=headers, json=body_json)
#
# print(response.text)

# ----------- Update Contact ----------
# ----------- Get Contact ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/contacts/64c7e1f12087310013816190'
#
# response = requests.get(url, headers=headers)
# print(response.text)
# ----------- Get Contact ----------

# ----------- Get User Profile ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/users/me'
#
# response = requests.get(url, headers=headers)
#
# print(response.text)
# ----------- Get User Profile ----------
# ----------- Update User ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/users/me'
# body_json = {
#     "firstName": "Updated",
#     "lastName": "Username",
#     "email": "pyta_2@itfactory.ro",
#     "password": "1234567"
# }
#
# response = requests.patch(url, headers=headers, json= body_json)
#
# print(response.text)
# ----------- Update User ----------
# ----------- Logout User ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/users/logout'
#
# response = requests.post(url, headers=headers)
#
# print(response.status_code)
# ----------- Logout User ----------
# ----------- Delete User ----------
# url = 'https://thinking-tester-contact-list.herokuapp.com/users/me'
#
# response = requests.delete(url, headers=headers)
#
# print(response.status_code)
# ----------- Delete User ----------
