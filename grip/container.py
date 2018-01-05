from grip.base import POPO


class Container(POPO):

    @staticmethod
    def from_dict(data):
        owner = data.pop('owner', {})
        extensions = data.pop('extensions', [])
        cont = Container(**data)
        return cont

    def to_payload(self):
        attrs = [
            'name',
            'description',
            'ref_code',
            'color',
            'type',
            'picture',
            'thumbnail'
        ]
        ret = {}
        for attr in attrs:
            ret[attr] = getattr(self, attr, '')

        return ret
