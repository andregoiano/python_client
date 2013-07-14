import urllib, requests, json

"""
Fosbury Python Client
"""

__version__ = '0.9'
__author__ = 'Willem Spruijt <willem@fosbury.co>'

class Client():
    """Initialize the Fosbury client"""
    def __init__(self, api_token, endpoint=None):
      self.api_token = api_token
      self.endpoint = "https://app.fosbury.co/api/v1/" if endpoint == None else endpoint
    
    # HTTP methods
    def get(self, url):
      r = requests.get(self.endpoint + url, headers=self.get_headers())
      return r.json()

    def post(self, url, post_params):
      r = request.post(self.endpoint + url, data=construct_payload(post_params), headers=self.get_headers())
      return r.json()

    def put(self, url, post_params):
      r = request.put(self.endpoint + url, data=construct_payload(post_params), headers=self.get_headers())
      return r.json()

    def delete(self, url):
      r = request.delete(self.endpoint + url, headers=self.get_headers())
      return r.json()

    def construct_payload(self, params):
      return urllib.urlencode(params)

    def get_headers(self):
      return {'X-Fosbury-Token': self.api_token}