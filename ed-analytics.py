import requests
from time import sleep
from settings import ACTOR_OBJECT_ID, ACCESS_TOKEN, ANALYTICS_URL

actor_id = ACTOR_OBJECT_ID
access_token = ACCESS_TOKEN
analytics_url = ANALYTICS_URL


def get_analytics_data():
    response = requests.get('{}{}'.format(analytics_url, actor_id, ),
                            headers={'Authorization': access_token,
                                     'content-type': 'application/json'})
    if response.status_code == 200:
        response = response.json()
        print ("# {}".format(response.get('count')))
        for _data in response.get('results'):
            model = None
            version = None
            if 'device' in _data.get('data').keys():
                model = _data.get('data').get('device').get('model')
                version = _data.get('data').get('device').get('version')

            response_format = "| {} | {} | {} | {} | {} | {} | {} |".format(
                    _data.get('timestamp'),
                    _data.get('data').get('network'),
                    _data.get('data').get('app_version'),
                    _data.get('actor_object_id'),
                    _data.get('verb'),
                    model,
                    version
                )

            print (response_format)

if __name__ == "__main__":
    while True:
        sleep(5)
        get_analytics_data()
        print ("\n\n\n")