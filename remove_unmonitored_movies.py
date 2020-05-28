#!/usr/local/bin/python3
"""Remove Unmonitored Movies in Radarr"""

from argparse import ArgumentParser, RawTextHelpFormatter
import requests

parser = ArgumentParser(
    description='You will need to provide an API Key and Base Url for Radarr',
    formatter_class=RawTextHelpFormatter
)

parser.add_argument(
    'apikey',
    type=str,
    help='Api Key for Radarr',
)

parser.add_argument(
    'baseurl',
    type=str,
    default='http://localhost:7878',
    help='Base url for Radarr, e.g. http://localhost:7878'
)

args = parser.parse_args()

api_key = args.apikey
headers = {"X-Api-Key": api_key}
url = args.baseurl
ENDPOINT = '/api/movie/'
complete_url = url + ENDPOINT

response = requests.get(complete_url, headers=headers)
data = response.json()

def remove_unmonitored_movies():

    """This will iterate through all movies and delete unmonitored by id"""

    for val in data:
        identifier = val['id']
        if val['monitored'] == False:
            payload = {'deleteFiles': False, 'addExclusion': False}
            requests.delete(complete_url + str(identifier), params=payload, headers=headers)

remove_unmonitored_movies()
