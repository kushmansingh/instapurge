import requests
import copy

from flask import jsonify, render_template, request, session
from instapurge import app

TOKEN_URL = 'https://api.instagram.com/oauth/access_token'
OAUTH_DATA = {'client_id': app.config['CLIENT_ID'],
              'client_secret':  app.config['CLIENT_SECRET'],
              'grant_type': 'authorization_code',
              'redirect_uri': app.config['REDIRECT_URL']}


@app.route('/')
def home():
    url = app.config['OAUTH_URL'].format(
        app.config['CLIENT_ID'], app.config['REDIRECT_URL'])
    return render_template('home.html', url=url)


@app.route('/redirect')
def redirect():
    code = request.args.get('code')
    data = copy.deepcopy(OAUTH_DATA)
    data['code'] = code
    resp = requests.post(TOKEN_URL, data=data)
    if not resp.ok:
        return render_template('error.html', error=resp.content)
    json = resp.json()
    session['access_token'] = json['access_token']
    return render_template('loading.html', user=json['user'])


@app.route('/followers')
def followers():
    url = 'https://api.instagram.com/v1/users/self/followed-by'
    access_token = session.get('access_token')
    if access_token is None:
        return render_template('error.html', error="Unauthorized")
    resp = requests.get(url, params=dict(access_token=access_token))
    import ipdb
    ipdb.set_trace()
    if not resp.ok:
        return render_template('error.html', error=resp.content)
    json = resp.json()
    return render_template('followers.html', followers=json['data'])
