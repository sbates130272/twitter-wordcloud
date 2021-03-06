#!/usr/bin/env python
#-------------------------------------------------------------------------------
#-
#-------------------------------------------------------------------------------
#-
#-
#-
#-------------------------------------------------------------------------------
#-
#-    Filename: example.py
#-
#-    Author:   Stephen Bates
#-    Project:  twitter-wordcloud
#-
#-  ---------------------------------------------------------------------------
#-
#-  Description
#-  -----------
#-    
#-
#------------------------------------------------------------------------------

import optparse
import twitter
import json
import pywordcloud

class OAuth():
    consumer_key        = ''
    consumer_secret     = ''
    access_token_key    = ''
    access_token_secret = ''

def GetOauth(OAuthFile):
    """Parse a file with the authorization presented as a JSON list. We do
    this to avoid having authentication details in this source code."""

    oauth = OAuth()
    with open(OAuthFile) as DataFile:
        data = json.load(DataFile)

    oauth.consumer_key        = data['consumer_key']
    oauth.consumer_secret     = data['consumer_secret']
    oauth.access_token_key    = data['access_token_key']
    oauth.access_token_secret = data['access_token_secret']

    return oauth

if __name__=="__main__":

    parser = optparse.OptionParser()
    parser.add_option("-s", "--search", action="store", default="ssd",
                      help="the search term passed into the Twitter API")
    parser.add_option("-n", "--count", action="store", default=15,
                      help="number of search terms to request (note API may limit this)")
    parser.add_option("-o", "--oauth", action="store", default="./oauth_example.json",
                      help="location of the file containing the OAuth information")
    parser.add_option("-v", "--verbose", action="store_true",
                      help="be verbose")
    (options, args) = parser.parse_args()

    oauth = GetOauth(options.oauth)

    api = twitter.Api(oauth.consumer_key, oauth.consumer_secret,
                      oauth.access_token_key, oauth.access_token_secret)

    search = api.GetSearch(term=options.search,
                           geocode=None,
                           since_id=None,
                           max_id=None,
                           until=None,
                           count=options.count,
                           lang='en',
                           locale=None,
                           result_type='mixed',
                           include_entities=None)

    text=[]    
    for res in search:
        text.append(res.text)
        if options.verbose:
            print res.text

    text = u''.join(text).encode('utf-8')
    if verbose:
        print text
    
    pywordcloud.create(text,
                       outfile="output.html",
                       uppercase=False,
                       showfreq=False,
                       frequency=100,
                       removepunct = True,
                       minfont = 1.5,
                       maxfont = 6,
                       hovercolor="green",
                       showborder=False,
                       fontfamily='calibri',
                       width="1000px",
                       height="400px")
    
