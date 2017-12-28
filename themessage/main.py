import logging
from themessage import medium_integration, medium_auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')


def main():
    # publish article
    # could use this example https://github.com/Medium/medium-sdk-python

    # If we don't have token, ask user to authorize
    token = None
    if not token:
        token = medium_auth.request_token()
        # TODO: store user's token and restore it next time when app will run

    # TODO: publish article by user token
    with open('examples/article.md') as f:
        md = f.read()
        # should try to extract from file.md
        # and file.yaml
        title = 'Test Article'
        # {
        #     'canonicalUrl': '',
        #     'license': 'all-rights-reserved',
        #     'title': 'My Title',
        #     'url': 'https://medium.com/@kylehg/55050649c95',
        #     'tags': ['python', 'is', 'great'],
        #     'authorId': '1f86...',
        #     'publishStatus': 'draft',
        #     'id': '55050649c95'
        # }
        res = medium_integration.publish(token, title, md)
        logger.info(f'Article available on {res["url"]}')


if __name__ == '__main__':
    logger.info('just before run main')
    main()
