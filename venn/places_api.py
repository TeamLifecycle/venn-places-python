import requests
from .exceptions import VennError


class PlacesAPI(object):

    def __init__(self, api_key, url="http://places.getvenn.io", version="1"):
        self.api_key = api_key
        self.url = url.strip("/")
        self.version = version
        self.search_endpoint = "search"

    def search(self, **params):
        """
        Perform a search. Either a keyword or category must be provided as well
        as either a location or an address.

        :param keyword: a keyword string
        :param category: a category string
        :param location: a (latitude, longitude) tuple  or comma separated string
        :param address: an address string
        :param limit: an integer limit of how man places to return
        """
        if "keyword" not in params and "category" not in params:
            raise ValueError("Must provide either a keyword or a category")
        elif "address" not in params and "location" not in params:
            raise ValueError("Must provide either an address or a location")
        if "location" in params:
            try:
                location = params["location"].split(",")
            except AttributeError:
                location = params["location"]
            try:
                if len(location) != 2:
                    raise ValueError("Location must be (latitude, longitude) pair")
            except TypeError:
                raise ValueError("Location must be (latitude, longitude) pair")
            params["location"] = ",".join([str(ll) for ll in location])
        params["key"] = self.api_key

        url = "/".join([self.url, "v"+self.version, self.search_endpoint])
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json().get("places", [])
        else:
            raise VennError(response)
