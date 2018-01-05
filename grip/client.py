import requests


class GRIPClient():

    def __init__(self, api_key):
        self.api_key = api_key

    def get_headers(self):
        """
        Get headers required to talk to GRIP API

        :return: dict
        """

        return {
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': 'Bearer %s' % self.api_key
        }
