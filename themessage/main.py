import logging
from themessage import markdown, medium_integration, medium_auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')


def main():
    # publish article
    # TODO: get token from arguments or env variables
    token = None

    # If we don't have token, ask user to authorize
    if not token:
        token = medium_auth.request_token()
        # TODO: store user's token and restore it next time when app will run

    with open('examples/article.md') as f:
        md = f.read()
        title = markdown.get_title(md) or 'New Article'
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
