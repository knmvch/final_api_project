import pytest


def test_get_nonexistent_meme(get_one_meme_endpoint):
    meme_id = 1313131313313
    get_one_meme_endpoint.get_one_meme(meme_id)
    get_one_meme_endpoint.check_that_status_is_404()


def test_update_nonexistent_meme(change_meme_endpoint):
    meme_id = 1313131313313
    body = {
        "text": "Invalid update",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme8.jpg",
        "tags": ["fail"],
        "info": {"year": 2021},
    }
    change_meme_endpoint.change_meme(body, meme_id)
    change_meme_endpoint.check_that_status_is_404()


def test_delete_nonexistent_meme(delete_meme_endpoint):
    meme_id = 1313131313313
    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_that_status_is_404()


def test_create_meme_with_empty_body(create_new_meme_endpoint):
    body = {}
    response = create_new_meme_endpoint.create_new_meme(body)

    if response.status_code == 200:
        create_new_meme_endpoint.check_field_text_contains_string()
        create_new_meme_endpoint.check_field_url_contains_string()
        create_new_meme_endpoint.check_field_tags_contains_array()
        create_new_meme_endpoint.check_field_info_contains_array()
    else:
        print(f"Error: Response status code {response.status_code}")

    create_new_meme_endpoint.check_bad_request()


def test_create_meme_invalid_types(create_new_meme_endpoint):
    body = {
        "text": 123,
        "url": 123,
        "tags": "not-a-list",
        "info": "just a string"
    }
    response = create_new_meme_endpoint.create_new_meme(body)

    if response.status_code == 200:
        try:
            create_new_meme_endpoint.check_field_text_contains_string()
        except AssertionError as error_in_test:
            print(f'{error_in_test}')

        try:
            create_new_meme_endpoint.check_field_url_contains_string()
        except AssertionError as error_in_test:
            print(f'{error_in_test}')

        try:
            create_new_meme_endpoint.check_field_tags_contains_array()
        except AssertionError as error_in_test:
            print(f'{error_in_test}')

        try:
            create_new_meme_endpoint.check_field_info_contains_array()
        except AssertionError as error_in_test:
            print(f'{error_in_test}')
    else:
        print(f"Error: Response status code {response.status_code}")

    create_new_meme_endpoint.check_bad_request()


def test_update_meme_with_invalid_types(change_meme_endpoint, meme_id):
    body = {
        "text": 123,
        "url": 123,
        "tags": "not-a-list",
        "info": "just a string"
    }
    response = change_meme_endpoint.change_meme(body, meme_id)

    if response.status_code == 200:
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
    else:
        print(f"Error: Response status code {response.status_code}")
