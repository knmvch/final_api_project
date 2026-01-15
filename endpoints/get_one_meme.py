import requests
from final_api_project.endpoints.endpoint import Endpoint


class GetOneMeme(Endpoint):
    def get_one_meme(self, meme_id):
        self.response = requests.get(
            f"{self.url}/meme/{meme_id}",
            headers=self.headers()
        )
        return self.response

    def get_one_meme_unauthorize(self, meme_id):
        self.response = requests.get(
            f"{self.url}/meme/{meme_id}",
        )
        return self.response

    def check_updated_text_is_text_in_response(
        self, get_one_meme_endpoint, meme_id, updated_text
    ):
        get_one_meme_endpoint.get_one_meme(meme_id)
        assert get_one_meme_endpoint.response.json()["text"] == updated_text

    def check_updated_url_is_url_in_response(
        self, get_one_meme_endpoint, meme_id, updated_url
    ):
        get_one_meme_endpoint.get_one_meme(meme_id)
        assert get_one_meme_endpoint.response.json()["url"] == updated_url

    def check_updated_tags_is_tags_in_response(
        self, get_one_meme_endpoint, meme_id, updated_tags
    ):
        get_one_meme_endpoint.get_one_meme(meme_id)
        assert get_one_meme_endpoint.response.json()["tags"] == updated_tags

    def check_updated_info_is_info_in_response(
        self, get_one_meme_endpoint, meme_id, updated_info
    ):
        get_one_meme_endpoint.get_one_meme(meme_id)
        assert get_one_meme_endpoint.response.json()["info"] == updated_info

    def check_get_meme_after_deleting_not_accessible(self, get_one_meme_endpoint, meme_id):
        get_one_meme_endpoint.get_one_meme(meme_id)
        assert get_one_meme_endpoint.response.status_code == 404

    def check_text_is_text_in_response(
        self, get_one_meme_endpoint, body
    ):
        assert get_one_meme_endpoint.response.json()["text"] == body["text"], 'Text in response is not text in request'

    def check_url_is_url_in_response(
        self, get_one_meme_endpoint, body
    ):
        assert get_one_meme_endpoint.response.json()["url"] == body["url"], 'Url in response is not url in request'

    def check_tags_is_tags_in_response(
        self, get_one_meme_endpoint, body
    ):
        assert get_one_meme_endpoint.response.json()["tags"] == body["tags"], 'Tags in response is not tags in request'

    def check_info_is_text_in_response(
        self, get_one_meme_endpoint, body
    ):
        assert get_one_meme_endpoint.response.json()["info"] == body["info"], 'Info in response is not info in request'
