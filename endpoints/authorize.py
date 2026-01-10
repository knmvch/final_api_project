import requests


class PostAuthorize:
    url = "http://memesapi.course.qa-practice.com"

    def __init__(self):
        self.response = None
        self.token = None

    def create_token(self, name="katyanaum"):
        self.response = requests.post(
            f"{self.url}/authorize",
            json={"name": name}
        )
        self.token = self.response.json()["token"]
        return self.token
