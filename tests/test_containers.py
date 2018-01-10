from grip_intros.container import Container
from tests.base import GripTestsBase


class TestContainer(GripTestsBase):

    def test_container_from_dict(self):
        data = {
            'name': 'Bongo',
            'description': 'Congo',
            'id': 23
        }
        instance = Container.from_dict(data)
        assert instance.name == 'Bongo'
        assert instance.description == 'Congo'
        assert instance.id == 23

    def test_container_payload(self):
        data = {
            'name': 'Bongo',
            'description': 'Congo',
            'id': 23
        }
        instance = Container.from_dict(data)
        payload = instance.to_payload()
        assert 'name' in payload
        assert payload['name'] == 'Bongo'
        assert 'picture' in payload
        assert payload['picture'] is None

    def test_container_add_thing(self,
                                 grip_test_client,
                                 example_container,
                                 thing_id):
        example_container.set_client(grip_test_client)
        response = example_container.add_thing(thing_id)
        assert response.get('data').get('message') == 'join created'

    def test_container_remove_thing(self,
                                    grip_test_client,
                                    example_container,
                                    thing_id):
        example_container.set_client(grip_test_client)
        response = example_container.remove_thing(thing_id)
        assert response.get('data').get('success') == 'connection deleted'
