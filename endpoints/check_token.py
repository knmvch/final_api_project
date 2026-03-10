import requests
from final_api_project.endpoints.endpoint import Endpoint


class CheckToken(Endpoint):
    def token_is_alive(self):
        self.response = requests.get(
            f"{self.url}/authorize/{self.token}"
        )
        return self.response.status_code == 200

    def check_token_is_alive(self):
        assert self.response.status_code == 200
