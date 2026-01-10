import requests
from final_api_project.endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):
    def get_all_memes(self):
        self.response = requests.get(
            f"{self.url}/meme",
            headers=self.headers()
        )
        return self.response

    def check_created_meme_in_memes_list(self, get_all_memes_endpoint, meme_id):
        meme_ids = [
            meme["id"] for meme in get_all_memes_endpoint.response.json()["data"]
        ]
        assert meme_id in meme_ids, "Created meme not found in memes list"

    def check_created_meme_not_in_memes_list(self, get_all_memes_endpoint, meme_id):
        meme_ids = [
            meme["id"] for meme in get_all_memes_endpoint.response.json()["data"]
        ]
        assert meme_id not in meme_ids, "Created meme found in memes list"
