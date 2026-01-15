class Endpoint:
    url = "http://memesapi.course.qa-practice.com"
    json = None

    def __init__(self, token):
        self.token = token
        self.response = None

    def headers(self):
        return {"Authorization": self.token}

    def check_that_status_is_200(self):
        assert self.response.status_code == 200, "Should return 200"

    def check_that_status_is_204(self):
        assert self.response.status_code == 204, "Should return 204"

    def check_that_status_is_401(self):
        assert self.response.status_code == 401, "Should return 401"

    def check_bad_request(self):
        assert self.response.status_code == 400, "Should return 400 for bad request"

    def check_that_status_is_404(self):
        assert self.response.status_code == 404, "Should return 404"

    def check_all_body_fields_filled(self):
        json_data = self.response.json()
        assert (
            json_data.get("text") and
            json_data.get("url") and
            json_data.get("tags") and
            json_data.get("info")
        ), "You must fill all of the fields"

    def check_field_contains_string(self):
        json_data = self.response.json()
        assert isinstance(json_data.get("text"), str), 'The "text" field must be of data type string'
        assert isinstance(json_data.get("url"), str), 'The "url" field must be of data type string'

    def check_field_tags_contains_array(self):
        json_data = self.response.json()
        assert isinstance(json_data.get("tags"), list), 'The "tags" field must be of data type array'

    def check_field_info_contains_array(self):
        json_data = self.response.json()
        assert isinstance(json_data.get("info"), dict), 'The "info" field must be of data type dictionary'

    def check_meme_id_in_response_json_is_meme_id(self, meme_id):
        assert self.response.json()["id"] == meme_id
