import requests
from final_api_project.endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    def delete_meme(self, meme_id):
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
            headers=self.headers()
        )
        return self.response

    def delete_meme_unauthorize(self, meme_id):
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
        )
        return self.response

    def delete_meme_unauthorized(self, meme_id):
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}"
        )
        return self.response
