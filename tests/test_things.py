from grip_intros.thing import Category
from tests.base import GripTestsBase
import responses


class TestThing(GripTestsBase):

    def test_thing_get_categories(self,
                                  grip_test_client,
                                  example_thing):
        example_thing.set_client(grip_test_client)
        categories = example_thing.get_categories()
        assert isinstance(categories, list)
        assert isinstance(categories[0], Category)
        assert categories[0]._client == grip_test_client

    def test_update_thing(self,
                          grip_test_client,
                          example_thing):

        grip_test_client.update_thing(example_thing.id, {'first_name': 'Roger'})
        assert responses.calls[0].request.url == 'https://api-test.intros.at/1/thing/7'
        assert responses.calls[0].request.body == b'{"first_name": "Roger"}'
