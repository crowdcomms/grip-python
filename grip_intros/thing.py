from grip_intros.base import POPO


class Thing(POPO):

    fields = [
        'name',
        'first_name',
        'last_name',
        'email',
        'headline',
        'summary',
        'job_title',
        'company_name',
        'job_industry',
        'gps_lat',
        'gps_lng',
        'location',
        'location_code',
        'categories',
        'picture_url',
        'matches',
        'subjects',
        'type_id',
        'metadata'
    ]

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_payload(self):
        result = {}
        for f in self.fields:
            result[f] = getattr(self, f, None)
        return result


class Category(POPO):
    pass