
class POPO(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_payload(self):
        return self.__dict__
