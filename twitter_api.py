"""
Module to get json dict with user's followers.
"""

import requests


def get_followers(username: str, bearer_token: str) -> dict:
    """
    Return dictionary with the information about user's followers
    >>> get_followers('barackobama', 'AAAAAAAA')
    {'errors': [{'code': 89, 'message': 'Invalid or expired token.'}]}
    """
    base_url = "https://api.twitter.com/"
    search_url = '{}1.1/friends/list.json'.format(base_url)
    search_headers = {
        'Authorization': 'Bearer {}'.format(bearer_token)
    }
    search_params = {
        'screen_name': '@'+username,
        'count': 50
    }
    response = requests.get(
        search_url, headers=search_headers, params=search_params)
    json_response = response.json()
    return json_response
