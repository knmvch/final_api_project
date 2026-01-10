import pytest


def test_create_new_meme(create_new_meme_endpoint, headers, json):
    create_new_meme_endpoint.create_new_meme(headers=headers,json=json)


def test_get_all_memes(get_one_meme_endpoint):
    get_one_meme_endpoint.get_one_meme()


def test_get_one_meme(get_all_memes_endpoint, meme_id):
    get_all_memes_endpoint.get_all_memes(meme_id)


def test_put_meme(change_meme_endpoint, meme_id):
    body = {
        "text": "Maybe very funny meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
        "tags": ["meme"],
        "info": {"year": 2019, "creater": "Raul", "famous": False}
    }
    change_meme_endpoint.change_meme(meme_id, body)


def test_delete_object(delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_meme(meme_id)
