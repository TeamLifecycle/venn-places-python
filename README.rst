Venn Places
===========

Get normalized place data from Foursquare, Yelp, Facebook, Google and Factual.

Installation
------------

::

    $ pip install venn-places

Usage
-----

::

    from venn import PlacesAPI

    api = PlacesAPI(venn_api_key)

    api.search(category="food",
               address="1411 Vine St. Cincinnati, OH 45202",
               limit=10)


Methods
-------

.search

=========  ================  ========================  ==================================
Parameter  Required          Type                      Example
=========  ================  ========================  ==================================
keyword    this or category  string                    outback
category   this or keyword   string                    food
address    this or location  string                    1411 Vine St. Cincinnati, OH 45202
location   this or address   string (comma separated)  44.2333423,-84.3453452
limit      no (default: 10)  int                       20
=========  ================  ========================  ==================================
