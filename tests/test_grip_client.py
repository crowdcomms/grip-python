from tests.base import GripTestsBase
from grip.container import Container


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
        assert payload['picture'] == ''


class TestGripClient(GripTestsBase):

    def test_build_uri(self, grip_client):
        url = grip_client.build_uri('container')
        assert url == 'https://api.intros.at/1/container'

    def test_get_headers(self, grip_client):
        headers = grip_client.get_headers()
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
        expected = 'Bearer %s' % grip_client.api_key
        assert headers.get('Authorization') == expected

    def test_list_containers(self, grip_test_client):
        containers = grip_test_client.list_containers()
        assert len(containers) == 1
        assert isinstance(containers, list)
        assert isinstance(containers[0], Container)

    def test_get_container(self, grip_test_client, container_id):
        container = grip_test_client.get_container(container_id)
        assert isinstance(container, Container)
        assert container.name == "Founders Forum"

    def test_create_container(self, grip_test_client):
        container = Container(
            name="fugiat aute cillum exercitation",
            type="private",
            color="#345345",
            picture="occaecat.jpg",
            thumbnail="incidid.jpg",
        )
        response = grip_test_client.create_container(container)
        assert isinstance(response, Container)
        assert hasattr(response, 'id')
