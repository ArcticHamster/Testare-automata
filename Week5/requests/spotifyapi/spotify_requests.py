import requests
from requests_oauth2client import *


class SpotifyRequests:
    _BASE_URL = "https://api.spotify.com/v1"
    _TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token"
    _GET_ALBUM_ENDPOINT = "/albums/"
    _GET_NEW_RELEASES_ENDPOINT = "/browse/new-releases"
    _AUTH_CLIENT_SECRET_AND_PASSWORD = ("829e5b82dd394a3ead21ea96c292415b", "043e6403f6784916b6aca61eec2db384")
    _CALLBACK_URI = "http://testitfactoryappta42"
    _TOKEN = ""

    _SCOPES = "ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing " \
              "app-remote-control streaming playlist-read-private playlist-read-collaborative " \
              "playlist-modify-private playlist-modify-public user-follow-modify user-follow-read " \
              "user-read-playback-position user-top-read user-read-recently-played user-library-modify " \
              "user-library-read user-read-email user-read-private"

    def __init__(self):
        self.generate_token()

    def generate_token(self):
        if len(self._TOKEN) < 1:
        # Instatam un client prin care obtinem token-ul
        # Clientul primeste ca parametri:
        # - token_endpoint - endpointul de generare al tokenului
        # - auth - tupla format client id si client secret
            oauth2client = OAuth2Client(token_endpoint=self._TOKEN_ENDPOINT, auth=self._AUTH_CLIENT_SECRET_AND_PASSWORD)
            self._TOKEN = f"Bearer {oauth2client.client_credentials(scope=self._SCOPES, resource=self._CALLBACK_URI)}"

        # print(self._TOKEN)

    def get_token(self):
        return self._TOKEN

    def get_header_auth(self):
        return {"Authorization": self.get_token()}

    def get_album(self, album_id):
        album_endpoint = self._BASE_URL + self._GET_ALBUM_ENDPOINT + album_id
        response = requests.get(album_endpoint, headers=self.get_header_auth())
        return response

    def get_new_release(self, country="", limit=""):
        new_release_endpoint = self._BASE_URL + self._GET_NEW_RELEASES_ENDPOINT

        if country == "" and limit != "":
            new_release_endpoint += f"?limit={limit}"
        elif country != "" and limit == "":
            new_release_endpoint += f"?country={country}"
        elif country != "" and limit != "":
            new_release_endpoint += f"?country={country}&limit={limit}"

        response = requests.get(new_release_endpoint, headers=self.get_header_auth())

        return response

# spotify = SpotifyRequests()
# spotify.generate_token()
# spotify.generate_token()
