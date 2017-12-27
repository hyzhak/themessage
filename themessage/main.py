import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

from themessage import medium_integration, medium_auth


def main():
    # publish article
    # could use this example https://github.com/Medium/medium-sdk-python

    # If we don't have token, ask user to authorize
    token = None
    if not token:
        token = medium_auth.request_token()
        # TODO: store user's token and restore it next time when app will run

    # TODO: publish article by user token
    pass


if __name__ == '__main__':
    logger.info('just before run main')
    main()
