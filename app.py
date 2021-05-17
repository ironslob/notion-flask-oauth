from flask import Flask, jsonify, redirect, url_for
from flask_dance.consumer import OAuth2ConsumerBlueprint
from werkzeug.middleware.proxy_fix import ProxyFix
import os

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = 'wombles'

client_id = os.environ.get('NOTION_OAUTH_CLIENT_ID')
client_secret = os.environ.get('NOTION_OAUTH_CLIENT_SECRET')

assert client_id, 'Must specify NOTION_OAUTH_CLIENT_ID environment variable'
assert client_secret, 'Must specify NOTION_OAUTH_CLIENT_SECRET environment variable'

notion_blueprint = OAuth2ConsumerBlueprint(
    "notion",
    __name__,
    client_id=client,
    client_secret=client_secret,
    base_url="https://api.notion.com",
    token_url="https://api.notion.com/v1/oauth/token",
    authorization_url="https://api.notion.com/v1/oauth/authorize",
)

app.register_blueprint(notion_blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not notion_blueprint.session.authorized:
        return redirect(url_for("notion.login"))

    session = notion_blueprint.session

    # see https://developers.notion.com/reference/get-users
    users = session.get('https://api.notion.com/v1/users')

    return jsonify(users.json())

if __name__ == '__main__':
    app.run(debug=True)
