import os 

DEBUG = True
HOST = "0.0.0.0"
CLIENT_ID = "e5984868b8704aebab8f1da1bf4833c9"
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
OAUTH_URL = "https://api.instagram.com/oauth/authorize/?client_id={}&redirect_uri={}&response_type=code&scope=follower_list+relationships"
REDIRECT_URL = "http://localhost:5000/redirect"
SECRET_KEY = os.urandom(24)