import os

DEBUG = False

SITE_NAME = "PMC Status Board"
SITE_AUTHOR = "PMC Engineering"
SITE_URL = "http://status.pmc.com"
REPORT_URL = "http://helpdesk.pmc.com/"

# Twitter update settings
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''
TWITTER_HANDLE = 'pmceng_status'

# RSS Feed settings
RSS_NUM_EVENTS_TO_FETCH = 50

# OAuth Consumer Credentials
CONSUMER_KEY = 'anonymous'
CONSUMER_SECRET = 'anonymous'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
    )
