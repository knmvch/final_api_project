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
        if 'application/json' in self.response.headers.get('Content-Type', ''):
            try:
                self.token = self.response.json().get("token")
                if not self.token:
                    print("Error: 'token' field is missing in the response.")
            except requests.exceptions.JSONDecodeError:
                print("Error: The response body is not JSON.")
                self.token = None
        else:
            print(f"Error: Expected JSON, but received {self.response.headers.get('Content-Type')}.")
            self.token = None

        return self.token

    def response_token(self, name="katyanaum"):
        self.response = requests.post(
            f"{self.url}/authorize",
            json={"name": name}
        )
        return self.response

    def check_bad_request(self):
        assert self.response.status_code == 400, "Should return 400 for bad request"

    def check_token_exists(self):
        assert "token" in self.response.json()

    def check_token_is_string(self):
        assert isinstance(self.response.json()["token"], str)

    def check_token_is_not_empty(self):
        assert len(self.response.json()["token"]) > 0

    def check_token_not_created(self):
        assert self.response is None

    def check_that_status_is_400(self):
        assert self.response.status_code == 400, "Should return 400"
