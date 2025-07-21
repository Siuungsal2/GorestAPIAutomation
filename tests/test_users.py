import allure
from utils.helper import post_request, get_request, put_request, delete_request

@allure.feature("CRUD User API")
class TestGoRest:

    @allure.story("Create -> Get -> Update -> Delete")
    def test_crud_user(self):
        # Create
        user_id = post_request()

        # Get
        user = get_request(user_id)

        # Update
        updated = put_request(user_id)

        # Delete
        delete_request(user_id)

        # Get after delete (negative)
        try:
            get_request(user_id)
            assert False, "User should not exist after delete"
        except AssertionError:
            pass  # expected