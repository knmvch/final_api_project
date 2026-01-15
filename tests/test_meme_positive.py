def test_meme_full_lifecycle(
    create_new_meme_endpoint,
    get_one_meme_endpoint,
    change_meme_endpoint,
    delete_meme_endpoint,
    meme_id,
):
    body = {
        "text": "Lifecycle meme",
        "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme8.jpg",
        "tags": ["qa"],
        "info": {"year": 2025},
    }
    create_new_meme_endpoint.create_new_meme(body)
    create_new_meme_endpoint.check_that_status_is_200()
    create_new_meme_endpoint.check_text_is_text_in_response(create_new_meme_endpoint, body)
    create_new_meme_endpoint.check_url_is_url_in_response(create_new_meme_endpoint, body)
    create_new_meme_endpoint.check_tags_is_tags_in_response(create_new_meme_endpoint, body)
    create_new_meme_endpoint.check_info_is_info_in_response(create_new_meme_endpoint, body)

    meme_id = create_new_meme_endpoint.response.json()["id"]

    get_one_meme_endpoint.get_one_meme(meme_id)
    get_one_meme_endpoint.check_that_status_is_200()

    updated_body = {
        "id": meme_id,
        "text": "Updated lifecycle meme",
        "url": body["url"],
        "tags": body["tags"],
        "info": body["info"],
    }
    change_meme_endpoint.change_meme(updated_body, meme_id)

    get_one_meme_endpoint.get_one_meme(meme_id)
    get_one_meme_endpoint.check_that_status_is_200()

    update_meme = get_one_meme_endpoint.response.json()

    change_meme_endpoint.check_updated_text_is_text_in_response(get_one_meme_endpoint, meme_id, update_meme["text"])
    change_meme_endpoint.check_updated_url_is_url_in_response(get_one_meme_endpoint, meme_id, update_meme["url"])
    change_meme_endpoint.check_updated_tags_is_tags_in_response(get_one_meme_endpoint, meme_id, update_meme["tags"])
    change_meme_endpoint.check_updated_info_is_info_in_response(get_one_meme_endpoint, meme_id, update_meme["info"])


    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_that_status_is_200()

    get_one_meme_endpoint.get_one_meme(meme_id)
    get_one_meme_endpoint.check_that_status_is_404()


def test_created_meme_appears_in_list(
   get_all_memes_endpoint,
   meme_id,
):
   get_all_memes_endpoint.get_all_memes()
   get_all_memes_endpoint.check_that_status_is_200()
   get_all_memes_endpoint.check_created_meme_in_memes_list(
       get_all_memes_endpoint, meme_id
   )


def test_meme_update_is_persisted(
    change_meme_endpoint,
    get_one_meme_endpoint,
    meme_id,
):
    updated_text = "New updated text"
    updated_url = (
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmzdBfP_qWdTtgMynUvWpGyc5jhZwlRFg5xg&s"
    )
    updated_tags = ["Updated tags"]
    updated_info = {"year": 2021}
    updated_body = {
        "id": meme_id,
        "text": updated_text,
        "url": updated_url,
        "tags": updated_tags,
        "info": updated_info,
    }
    change_meme_endpoint.change_meme(updated_body, meme_id)

    get_one_meme_endpoint.get_one_meme(meme_id)
    get_one_meme_endpoint.check_that_status_is_200()

    update_meme = get_one_meme_endpoint.response.json()

    get_one_meme_endpoint.check_updated_text_is_text_in_response(
        get_one_meme_endpoint, meme_id, update_meme["text"]
    )
    get_one_meme_endpoint.check_updated_url_is_url_in_response(
        get_one_meme_endpoint, meme_id, update_meme["url"]
    )
    get_one_meme_endpoint.check_updated_tags_is_tags_in_response(
        get_one_meme_endpoint, meme_id, update_meme["tags"]
    )
    get_one_meme_endpoint.check_updated_info_is_info_in_response(
        get_one_meme_endpoint, meme_id, update_meme["info"]
    )


def test_deleted_meme_is_not_accessible(
   create_new_meme_endpoint,
   delete_meme_endpoint,
   get_one_meme_endpoint,
   get_all_memes_endpoint,
   meme_id,
):
   body = {
       "text": "Delete me",
       "url": "https://mailtrap.io/wp-content/uploads/2020/06/testing_meme8.jpg",
       "tags": ["delete"],
       "info": {"year": 2020},
   }
   create_new_meme_endpoint.create_new_meme(body)
   meme_id = create_new_meme_endpoint.response.json()["id"]

   delete_meme_endpoint.delete_meme(meme_id)
   delete_meme_endpoint.check_that_status_is_200()

   get_all_memes_endpoint.get_all_memes()
   get_all_memes_endpoint.check_created_meme_not_in_memes_list(
       get_all_memes_endpoint, meme_id
   )

   get_one_meme_endpoint.check_get_meme_afted_deliting_not_accessible(
       get_one_meme_endpoint, meme_id
   )
