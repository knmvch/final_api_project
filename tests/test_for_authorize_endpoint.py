import pytest
from final_api_project.endpoints.authorize import PostAuthorize
from final_api_project.endpoints.check_token import CheckToken


def test_create_token(create_token_endpoint):
    response = create_token_endpoint.response_token()
    assert 'token' in response.json(), "Token is missing in the response"
    token = response.json()['token']
    assert isinstance(token, str), "Token is not a string"
    assert len(token) > 0, "Token length is zero"

def test_token_is_alive(token):
    check_token_endpoint = CheckToken(token=token)
    result = check_token_endpoint.token_is_alive()
    assert result, "Token is not alive"

def test_invalid_token():
    invalid_token = "invalid-token"
    check_token_endpoint = CheckToken(token=invalid_token)
    check_token_endpoint.token_is_alive()
    check_token_endpoint.check_that_status_is_404()


def test_create_token_with_wrong_params():
    authorizer = PostAuthorize()
    wrong_name = 1233
    token = authorizer.create_token(wrong_name)

    assert token is None
