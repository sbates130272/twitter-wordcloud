twitter-wordcloud
=================

Generates a wordcloud based on popular words in tweets related to the
input keyword(s)

Pre-requisties
--------------

This code-base relies on the python-twitter module
(http://code.google.com/p/python-twitter/). See its README.md for
installation and for setting up the OAuth required for Twitter API
1.1. The code also relies on the pywordcloud package which is
available from (https://github.com/shivam5992/pywordcloud.git).  


Usage
-----

Run ./example.py -h to see usage.

Example
-------

$ ./example.py -o ../oauth.json -v -s flash
