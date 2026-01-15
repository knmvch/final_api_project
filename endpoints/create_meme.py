import requests
from final_api_project.endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    def create_new_meme(self, body):
        self.response = requests.post(
            f"{self.url}/meme",
            json=body,
            headers=self.headers()
        )
        return self.response

    def create_new_meme_unauthorize(self, body):
        self.response = requests.post(
            f"{self.url}/meme",
            json=body,
        )
        return self.response

    def check_text_is_text_in_response(
        self, create_new_meme_endpoint, body
    ):
        assert create_new_meme_endpoint.response.json()["text"] == body["text"], 'Text in response is not text in request'

    def check_url_is_url_in_response(
        self, create_new_meme_endpoint, body
    ):
        assert create_new_meme_endpoint.response.json()["url"] == body["url"], 'Url in response is not url in request'

    def check_tags_is_tags_in_response(
        self, create_new_meme_endpoint, body
    ):
        assert create_new_meme_endpoint.response.json()["tags"] == body["tags"], 'Tags in response is not tags in request'

    def check_info_is_info_in_response(
        self, create_new_meme_endpoint, body
    ):
        assert create_new_meme_endpoint.response.json()["info"] == body["info"], 'Info in response is not info in request'
