import pytest

from final_api_project.endpoints.change_meme import ChangeMeme
from final_api_project.endpoints.create_meme import CreateMeme
from final_api_project.endpoints.delete_meme import DeleteMeme
from final_api_project.endpoints.get_all_memes import GetAllMemes
from final_api_project.endpoints.get_one_meme import GetOneMeme


@pytest.fixture()
def create_new_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def change_meme_endpoint():
    return ChangeMeme()


@pytest.fixture()
def get_all_memes_endpoint():
    return GetAllMemes()


@pytest.fixture()
def get_one_meme_endpoint():
    return GetOneMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def meme_id(create_new_meme_endpoint, delete_meme_endpoint):
    body = {
        "text": "Very funny meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
        "tags": ["meme", "qa", "IT", "work"],
        "info": {"year": 2018, "creater": "Paul", "famous": True}
    }
    create_new_meme_endpoint.create_new_meme(body)
    yield create_new_meme_endpoint.meme_id
    delete_meme_endpoint.delete_meme(meme_id)
