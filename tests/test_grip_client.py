from tests.base import GripTestsBase


class TestGripClient(GripTestsBase):

    def test_get_headers(self, grip_client):
        headers = grip_client.get_headers()
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
        expected = 'Bearer %s' % grip_client.api_key
        assert headers.get('Authorization') == expected
