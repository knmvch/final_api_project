import pytest
from final_api_project.endpoints.authorize import PostAuthorize
from final_api_project.endpoints.check_token import CheckToken


def test_create_token(create_token_endpoint):
    create_token_endpoint.response_token()
    create_token_endpoint.check_token_exists()
    create_token_endpoint.check_token_is_string()
    create_token_endpoint.check_token_is_not_empty()

def test_token_is_alive(token):
    check_token_endpoint = CheckToken(token=token)
    check_token_endpoint.token_is_alive()
    check_token_endpoint.check_token_is_alive()

def test_invalid_token():
    invalid_token = "invalid-token"
    check_token_endpoint = CheckToken(token=invalid_token)
    check_token_endpoint.token_is_alive()
    check_token_endpoint.check_that_status_is_404()


def test_create_token_with_wrong_params():
    authorizer = PostAuthorize()
    wrong_name = 1233
    authorizer.create_token(wrong_name)
    authorizer.check_that_status_is_400()
