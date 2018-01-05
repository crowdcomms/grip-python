import json

import requests

from grip.container import Container


class GRIPClient():

    def __init__(self, api_key, test_mode=False):
        self.api_key = api_key
        if test_mode:
            self.base_uri = 'https://api-test.intros.at/1/'
        else:
            self.base_uri = 'https://api.intros.at/1/'

    def build_uri(self, path):
        return "%s%s" % (self.base_uri, path)

    def get(self, url):
        request = requests.get(url, headers=self.get_headers())
        request.raise_for_status()
        return request.json().get('data')

    def post(self, url, payload={}, headers={}):
        final_headers = self.get_headers()
        final_headers.update(headers)
        request = requests.post(url, json=payload, headers=final_headers)
        request.raise_for_status()
        return request.json()

    def patch(self, url, payload={}, headers={}):
        final_headers = self.get_headers()
        final_headers.update(headers)
        request = requests.patch(url, json=payload, headers=final_headers)
        request.raise_for_status()
        return request.json()

    def delete(self, url, headers={}):
        final_headers = self.get_headers()
        final_headers.update(headers)
        request = requests.delete(url, headers=final_headers)
        request.raise_for_status()
        return request.json()

    def get_headers(self):
        """
        Get headers required to talk to GRIP API

        :return: dict
        """

        return {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.api_key
        }

    def list_containers(self):
        url = self.build_uri('container')
        response = self.get(url)
        return [Container.from_dict(data) for data in response]

    def get_container(self, container_id):
        url = self.build_uri('container/%i' % container_id)
        response = self.get(url)
        return Container.from_dict(response)

    def create_container(self, container):
        url = self.build_uri('container')
        payload = container.to_payload()
        response = self.post(url, payload)
        return Container.from_dict(response)
