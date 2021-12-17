from src.utilities.genericUtilities import generate_random_email_and_password
from src.utilities.requestsUtility import RequestsUtility

class CustomerHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'

        body = dict()
        body['email'] = email
        body['password'] = password
        body.update(kwargs)

        create_user_json = self.requests_utility.post('customers', body_params=body, headers=None, expected_status_code=201)
        return create_user_json
