import random
import requests


class SimpleBooksRequests:
    _BASE_URL = "https://simple-books-api.glitch.me"
    _API_STATUS_ENDPOINT = "/status"
    _GET_ALL_BOOKS_ENDPOINT = "/books"
    _API_AUTH_ENDPOINT = "/api-clients/"
    _ORDERS_ENDPOINT = "/orders"

    def get_api_status(self):
        api_status_url = self._BASE_URL + self._API_STATUS_ENDPOINT
        response = requests.get(api_status_url)
        return response

    def get_all_books(self, book_type="", limit=""):
        get_all_books_url = self._BASE_URL + self._GET_ALL_BOOKS_ENDPOINT

        if book_type != "" and limit == "":
            get_all_books_url += f"?type={book_type}"
        elif book_type == "" and limit != "":
            get_all_books_url += f"?limit={limit}"
        elif book_type != "" and limit != "":
            get_all_books_url += f"?type={book_type}&limit={limit}"

        response = requests.get(get_all_books_url)

        return response

    def generate_token(self):
        auth_url = self._BASE_URL + self._API_AUTH_ENDPOINT

        random_number = random.randint(1, 999999999999999999999999999999999)

        request_body = {
            "clientName": "PYTA2",
            "clientEmail": f"pyta2_client{random_number}@itfactory.ro"
        }

        response = requests.post(auth_url, json=request_body)

        return response.json()['accessToken']

    def submit_order(self, access_token, book_id, customer_name):
        submit_orders_url = self._BASE_URL + self._ORDERS_ENDPOINT

        header_params = {"Authorization": access_token}

        request_body = {
            "bookId": book_id,
            "customerName": customer_name
        }

        response = requests.post(submit_orders_url, json=request_body, headers=header_params)

        return response

    def update_order(self, access_token, order_id, new_customer_name):
        order_update_url =  self._BASE_URL + self._ORDERS_ENDPOINT + f"/{order_id}"

        header_params = {"Authorization": access_token}

        request_body = {
            "customerName": new_customer_name
        }

        response = requests.patch(order_update_url, json=request_body, headers=header_params)

        return response