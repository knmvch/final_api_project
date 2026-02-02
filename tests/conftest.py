import pytest

from final_api_project.endpoints.authorize import PostAuthorize
from final_api_project.endpoints.check_token import CheckToken
from final_api_project.endpoints.change_meme import ChangeMeme
from final_api_project.endpoints.create_meme import CreateMeme
from final_api_project.endpoints.delete_meme import DeleteMeme
from final_api_project.endpoints.get_all_memes import GetAllMemes
from final_api_project.endpoints.get_one_meme import GetOneMeme


@pytest.fixture(scope="session")
def token():
    auth = PostAuthorize()
    token = auth.create_token()

    checker = CheckToken(token)
    if not checker.token_is_alive():
        token = auth.create_token()

    return token

@pytest.fixture()
def create_token_endpoint():
    return PostAuthorize()

@pytest.fixture()
def create_new_meme_endpoint(token):
    return CreateMeme(token)


@pytest.fixture()
def change_meme_endpoint(token):
    return ChangeMeme(token)


@pytest.fixture()
def get_all_memes_endpoint(token):
    return GetAllMemes(token)


@pytest.fixture()
def get_one_meme_endpoint(token):
    return GetOneMeme(token)


@pytest.fixture()
def delete_meme_endpoint(token):
    return DeleteMeme(token)


@pytest.fixture()
def meme_id(create_new_meme_endpoint, delete_meme_endpoint):
    body = {
        "text": "Very funny meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
        "tags": ["meme", "qa", "IT", "work"],
        "info": {"year": 2018, "creater": "Paul", "famous": True}
    }
    response = create_new_meme_endpoint.create_new_meme(body)
    meme_id = response.json()["id"]
    yield meme_id
    delete_meme_endpoint.delete_meme(meme_id)
