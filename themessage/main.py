import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

from flask import Flask, jsonify
import medium
import os
from themessage import medium_integration, server

app = Flask(__name__)
app.register_blueprint(server.medium_blueprint, url_prefix='/medium')


@app.route('/')
def root_router():
    return jsonify({'status': 'ok'})


# Go to http://medium.com/me/applications to get your application_id and application_secret.
client = medium.Client(application_id=os.environ.get('MEDIUM_APP_ID'),
                       application_secret=os.environ.get('MEDIUM_APP_SECRET'))


def publish(authorization_code):
    # Exchange the authorization code for an access token (maybe jwt?).
    auth = client.exchange_authorization_code(authorization_code,
                                              os.environ.get('MEDIUM_APP_CALLBACK_URL'))

    # The access token is automatically set on the client for you after
    # a successful exchange, but if you already have a token, you can set it
    # directly.
    client.access_token = auth['access_token']

    # Get profile details of the user identified by the access token.
    user = client.get_current_user()

    # Create a draft post.
    post = client.create_post(user_id=user['id'], title='Title', content='<h2>Title</h2><p>Content</p>',
                              content_format='html', publish_status='draft')

    # When your access token expires, use the refresh token to get a new one.
    # client.exchange_refresh_token(auth['refresh_token'])

    # Confirm everything went ok. post['url'] has the location of the created post.
    logger.info('My new post!', post['url'])


def main():

    # publish article
    # could use this example https://github.com/Medium/medium-sdk-python

    auth_url = medium_integration.get_url()

    logger.info(f'[!] tap here: {auth_url}')

    port_string = os.environ.get('SERVER_PORT', None)
    port = int(port_string) if port_string else None

    app.run(host=os.environ.get('SERVER_IP', '0.0.0.0'),
            port=port,
            debug=os.environ.get('SERVER_DEBUG', '').lower() == 'true',
            )

    # (Send the user to the authorization URL to obtain an authorization code.)


if __name__ == '__main__':
    logger.info('just before run main')
    main()
