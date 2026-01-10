import requests
from final_api_project.endpoints.endpoint import Endpoint


class PostAuthorize(Endpoint):
    body = {
        "name": "katyanaum"
    }
    headers = None
    def create_token(self, body):
        response = requests.post(f'{self.url}/authorize', json=body)
        self.token = response.json()['token']
        self.url = response.json()['url']
        return self.token, self.url
