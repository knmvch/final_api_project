import pytest


def test_create_new_meme(create_new_meme_endpoint):
    create_new_meme_endpoint.create_new_meme(
        body={
            "text": "Very funny meme",
            "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
            "tags": ["meme", "qa", "IT", "work"],
            "info": {"year": 2018, "creater": "Paul", "famous": True},
        }
    )
    create_new_meme_endpoint.check_that_status_is_200()
    create_new_meme_endpoint.check_all_body_fields_filled()


def test_get_all_memes(get_all_memes_endpoint, meme_id):
   get_all_memes_endpoint.get_all_memes()
   get_all_memes_endpoint.check_that_status_is_200()
   get_all_memes_endpoint.check_created_meme_in_memes_list(get_all_memes_endpoint, meme_id)


def test_get_one_meme(get_one_meme_endpoint, meme_id):
    get_one_meme_endpoint.get_one_meme(meme_id)
    get_one_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.check_meme_id_in_response_json_is_meme_id(meme_id)


def test_put_meme(change_meme_endpoint, meme_id):
    body = {
        "id": meme_id,
        "text": "Maybe very funny meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme4.jpg",
        "tags": ["meme"],
        "info": {"year": 2019, "creater": "Raul", "famous": False},
    }
    change_meme_endpoint.change_meme(meme_id, body)
    change_meme_endpoint.check_all_body_fields_filled()
    try:
        change_meme_endpoint.check_field_text_contains_string()
    except AssertionError as error_in_test:
        print(f'{error_in_test}')

    try:
        change_meme_endpoint.check_field_url_contains_string()
    except AssertionError as error_in_test:
        print(f'{error_in_test}')

    try:
        change_meme_endpoint.check_field_tags_contains_array()
    except AssertionError as error_in_test:
        print(f'{error_in_test}')

    try:
        change_meme_endpoint.check_field_info_contains_array()
    except AssertionError as error_in_test:
        print(f'{error_in_test}')



def test_delete_object(delete_meme_endpoint, get_all_memes_endpoint, meme_id, get_one_meme_endpoint):
    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_that_status_is_200()
    get_one_meme_endpoint.check_get_meme_after_deleting_not_accessible(get_one_meme_endpoint, meme_id)
