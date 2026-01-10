import requests
from final_api_project.endpoints.post_authorize import PostAuthorize


class GetAuthorize(PostAuthorize):
    def get_token (self, token):
        self.response = requests.get(f'{self.url}/{token}')
        return self.response.status_code
