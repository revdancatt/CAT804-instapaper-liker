#!/usr/bin/env python
import webapp2
import json
from google.appengine.api import urlfetch

_USERNAME = 'YOUR USERNAME'  # probably your email adress
_PASSWORD = 'YOUR INSTAPAPER PASSWORD'  # if you have one, no idea what happens if you don't


class MainHandler(webapp2.RequestHandler):
    def get(self):

        #   Go and get the unliked pages from instagram
        url = 'http://www.instapaper.com/api/1/bookmarks/list?username=%s&password=%s' % (_USERNAME, _PASSWORD)

        #   Now go fetch it
        #   TODO, put your error checking in here!!
        result = urlfetch.fetch(url=url)
        result = json.loads(result.content)

        #   Assuming everything went well we now have a valid JSON
        #   response. Let's loop thru all the items looking for
        #   bookmarks
        for item in result:

            #   make sure it has a type, and if so that it's
            #   a bookmark
            if 'type' in item and item['type'] == 'bookmark':

                #   Ok, now check to see if it isn't already starred
                if 'starred' in item and item['starred'] == '0' and 'bookmark_id' in item:

                    #   call the "star" API endpoint
                    #   TODO add slightly better error checking here.
                    #   This is only really a problem for the first time
                    #   this is run and there may be a large number (at
                    #   most 25) of unstarred items. After that the
                    #   cron job is going to run once every 10mins, so
                    #   unless you're a crazy twitter faver this should
                    #   catch them roughly as they come in
                    try:
                        urlfetch.fetch(url='http://www.instapaper.com/api/1/bookmarks/star?username=%s&password=%s&bookmark_id=%s' % (_USERNAME, _PASSWORD, item['bookmark_id']))
                    except:
                        continue


app = webapp2.WSGIApplication([
    ('/cron/checkBookmarks', MainHandler)
], debug=True)
