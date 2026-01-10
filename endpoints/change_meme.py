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
