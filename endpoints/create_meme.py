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
