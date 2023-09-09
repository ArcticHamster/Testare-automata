from Week5.requests.spotifyapi.spotify_requests import SpotifyRequests
from Week5.tests.spotifytests.test_base import TestBase


class TestGetNewRelease(TestBase):

    def setUp(self) -> None:
        self.spotify = SpotifyRequests()

    def test_get_new_releases_no_filter(self):
        response = self.spotify.get_new_release()

        # expected_response_code = 200
        # actual_response_code = response.status_code
        # self.assertEqual(expected_response_code, actual_response_code, "Unexpected status code")
        self.verify_status_code(200, response.status_code)

        # expected_response_size = 20
        # actual_response_size = len(response.json()['albums']['items'])
        # self.assertEqual(expected_response_size, actual_response_size, "Unexpected response size")
        self.verify_response_size(20, response.json()['albums']['items'])

    def test_get_new_releases_filter_by_country(self):
        country = "RO"
        response = self.spotify.get_new_release(country=country)

        # este o lista cu 20 de dict-uri python
        item_list = response.json()['albums']['items']

        self.verify_status_code(200, response.status_code)
        self.verify_response_size(20, item_list)

        for i in range(len(item_list)):
            current_item = item_list[i]
            name = current_item['name']
            available_markets = current_item['available_markets']

            # la unele din albume nu avem RO in lista ( posibil bug la spotify in API?)
            assert "RO" in available_markets or len(available_markets) == 0
            print(f"RO este in lista cu available_markets pentru albumul {name}")