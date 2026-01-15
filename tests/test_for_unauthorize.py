def test_post_meme_without_authorization(create_new_meme_endpoint):
    create_new_meme_endpoint.create_new_meme_unauthorize(
        body={
            "text": "Very funny meme",
            "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
            "tags": ["meme", "qa", "IT", "work"],
            "info": {"year": 2018, "creater": "Paul", "famous": True},
        }
    )
    create_new_meme_endpoint.check_that_status_is_401()

def test_put_meme_without_authorization(change_meme_endpoint, meme_id):
    change_meme_endpoint.change_meme_unauthorize(
        body = {
        "id": meme_id,
        "text": "Maybe very funny meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
        "tags": ["meme"],
        "info": {"year": 2019, "creater": "Raul", "famous": False},
    },
        meme_id=meme_id
    )
    change_meme_endpoint.check_that_status_is_401()

def test_delete_meme_without_authorization(delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_meme_unauthorize(meme_id)
    delete_meme_endpoint.check_that_status_is_401()

def test_get_all_meme_without_authorization(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes_unauthorize()
    get_all_memes_endpoint.check_that_status_is_401()

def test_get_one_meme_without_authorization(get_one_meme_endpoint, meme_id):
    get_one_meme_endpoint.get_one_meme_unauthorize(meme_id)
    get_one_meme_endpoint.check_that_status_is_401()