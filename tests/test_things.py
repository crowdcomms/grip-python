from grip_intros.thing import Category

from tests.base import GripTestsBase


class TestThing(GripTestsBase):

    def test_thing_get_categories(self,
                                  grip_test_client,
                                  example_thing):
        example_thing.set_client(grip_test_client)
        categories = example_thing.get_categories()
        assert isinstance(categories, list)
        assert isinstance(categories[0], Category)
        assert categories[0]._client == grip_test_client
