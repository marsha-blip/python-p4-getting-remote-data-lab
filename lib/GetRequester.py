import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Makes a GET request to self.url and returns the *bytes* body of the response.
        """
        response = requests.get(self.url)
        response.raise_for_status()  # optional, but good: will raise an error on bad status codes
        # response.content returns raw bytes
        return response.content

    def load_json(self):
        """
        Uses get_response_body to get the response, then parses the JSON and returns the Python data.
        """
        body_bytes = self.get_response_body()
        # We need to decode bytes to string before json.loads, typically using UTF-8
        # Or requests also has a response.json(), but since test expects you to use the above pattern:
        text = body_bytes.decode('utf-8')
        data = json.loads(text)
        return data
