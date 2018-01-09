import responses
from requests.status_codes import codes
import re
import os


base_url = 'https://api-test.intros.at/1'

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'responses')

examples = {}

for item in os.listdir(path):
    if item.endswith('.json'):
        fname, ext = os.path.splitext(item)
        with open(os.path.join(path, item), 'r') as f:
            examples[fname] = f.read()


class GripTestsBase():
    default_uri = re.compile('%s/(\w+)' % (base_url))

    requests_mock = {
        'test_list_containers': {
            'uri': '%s/container' % base_url,
            'body': '{"success":true,"data":[{"id":17732,"name":"Test"}]}'
        },
        'test_get_container': {
            'uri': re.compile('%s/container/\d+' % base_url),
            'body': examples['test_get_container']
        },
        'test_create_container': {
            'uri': '%s/container' % base_url,
            'body': examples['test_create_container'],
            'method': responses.POST
        },
        'test_base_url_auto': {
            'uri': '%s/container' % base_url,
            'body': '{"success":true,"data":[{"id":17732,"name":"Test"}]}'
        },
        'test_get_container_things': {
            'uri': re.compile('%s/container/\d+/thing' % base_url),
            'body': examples['test_get_container_things']
        },
        'test_get_thing_detail': {
            'uri': re.compile('%s/thing/\d+' % base_url),
            'body': examples['test_get_thing_detail']
        },
        'test_get_categories': {
            'uri': '%s/thing/category' % base_url,
            'body': examples['test_get_categories']
        },
        'test_create_thing_from_thing': {
            'uri': '%s/thing' % base_url,
            'body': examples['test_create_thing_from_thing'],
            'method': responses.POST
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
