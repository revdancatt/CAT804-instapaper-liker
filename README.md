CAT804-instapaper-liker
=======================

A tiny AppEngine python cron job to look through the latest 25 bookmarks in an instapaper account and star/like all the ones that haven't been starred/liked. Checks every 10 minutes. You'll need to add your own _USERNAME and _PASSWORD

# Why?

Because when I star/fave a tweet containing a link, I want a full copy of the page linked to placed into Evernote, so when I use the Evernote Chrome extension those pages will show up in my Google search results.

There's a way fairly simple way to _nearly_ automated way of capturing full pages faved on twitter into Evernote but it's missing a single step, this fills in that gap.

The process involves IFTTT.

1. IFTTT can't have twitter as a trigger/input so we need some way to spot starred/faved tweets.
2. pinboard.in will spot links in faved tweets and bookmark the target page, but there's no simple way to get the full page content into Evernote.
3. So IFTTT spots bookmarks in pinboard.in and copies them across to Instapaper
4. [MISSING STEP]
5. Instapaper can be setup to email the full page from a link to Everynote, but it only does this for links that you star/like
6. Evernote gets the emails from Instapaper and does it's awesome thing with it.

The missing step is that pinboard can push the links to Instapaper, but Instapaper only pushed the stared/liked ones to Everynote.

This cronjob automatically stars/likes all links put into Instapaper thus
bridging the gap needed to get them into Evernote.

Or at least until I work out a better way.