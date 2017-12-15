import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

from themessage import medium_integration


def main():
    # publish article
    # could use this example https://github.com/Medium/medium-sdk-python

    # If we don't have token, ask user to authorize

    auth_url = medium_integration.get_url()

    logger.info(f'[!] tap here: {auth_url}')


if __name__ == '__main__':
    logger.info('just before run main')
    main()
