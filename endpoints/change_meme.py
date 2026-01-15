import requests
from final_api_project.endpoints.endpoint import Endpoint


class ChangeMeme(Endpoint):
    def change_meme(self, meme_id, body):
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            json=body,
            headers=self.headers()
        )
        return self.response

    def change_meme_unauthorize(self, body, meme_id,):
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            json=body,
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