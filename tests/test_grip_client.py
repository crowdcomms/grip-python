from tests.base import GripTestsBase
from grip_intros.container import Container
from grip_intros.thing import Category, Thing


class TestGripClient(GripTestsBase):

    def test_build_uri(self, grip_client):
        url = grip_client.build_uri('container')
        assert url == 'https://api.intros.at/1/container'

    def test_base_url_auto(self, grip_test_client):
        response = grip_test_client.get('/container')
        assert response == {
            'data': [{'id': 17732, 'name': 'Test'}], 'success': True
        }

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
        assert containers[0]._client == grip_test_client

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
        assert response._client == grip_test_client
        assert hasattr(response, 'id')

    def test_get_container_things(self, grip_test_client, container_id):
        things = grip_test_client.get_things(container_id)
        assert isinstance(things, list)
        assert len(things) == 5
        assert things[0]._client == grip_test_client

    def test_get_thing_detail(self, grip_test_client, thing_id):
        thing = grip_test_client.get_thing(thing_id)
        assert thing.job_title == 'CEO'
        assert thing._client == grip_test_client

    def test_get_categories(self, grip_test_client):
        categories = grip_test_client.get_categories()
        assert isinstance(categories[0], Category)
        assert categories[0]._client == grip_test_client
        assert len(categories) == 3

    def test_thing_payload(self):
        thing = Thing(
            first_name="Test",
            last_name="User",
            job_industry="Automotive",
            email="test@example.com"
        )

        payload = thing.to_payload()
        assert 'job_industry' in payload
        assert payload['job_industry'] == 'Automotive'

    def test_create_thing_from_thing(self, grip_test_client):
        data = {
          "name": "Jo Somebody",
          "first_name": "Jo",
          "last_name": "Somebody",
          "email": "jo@grip.events",
          "headline": "My headline goes here",
          "summary": " I am Jo Somebody from Grip",
          "job_title": "TestBot at Grip",
          "company_name": "Grip Technologies Limited",
          "job_industry": "Information Technology",
          "gps_lat": 55.666084,
          "gps_lng": 55.666084,
          "location": "London",
          "location_code": "en-gb",
          "categories": [
            "cloud computing",
            "real estate"
          ],
          "picture_url": "https://some.domain/picture.jpg",
          "matches": [
            "accountants ",
            "startups",
            "investors"
          ],
          "subjects": [
            "fintech",
            "AI",
            "emerging markets"
          ],
          "type_id": 1234,
          "metadata": "{\"some_key\": \"some_value\"}"
        }
        thing = Thing.from_dict(data)
        assert isinstance(thing, Thing)
        thing = grip_test_client.create_thing(thing)
        assert thing._client == grip_test_client
        assert hasattr(thing, 'id')
        assert isinstance(thing.id, int)
