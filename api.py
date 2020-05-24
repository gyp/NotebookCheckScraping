# Libraries
from contextlib import closing
from requests import get
from requests.exceptions import RequestException


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()

    return (
        resp.status_code == 200 and
        content_type is not None and
        content_type.find('html') > -1
    )
