import responses
from requests.status_codes import codes
import re

base_url = 'https://api-test.intros.it/1'


class GripTestsBase():

    default_uri = re.compile('%s/(\w+)' % base_url)

    requests_mock = {
        'test_list_containers': {
            'uri': '%s/container',
            'body': '{"success":true,"data":[{"id":17732,"name":"Test"}]}'
        }
    }

    def setup_method(self, method):
        responses.start()
        request_data = self.requests_mock.get(method.__name__, {})

        responses.add(
            method=request_data.get('method', responses.GET),
            url=request_data.get('uri', self.default_uri),
            body=request_data.get('body', '{}'),
            status=request_data.get('status', codes.ok),
            content_type=request_data.get('content_type', 'application/json')
        )

    def teardown_method(self, method):
        responses.reset()
        responses.stop()
