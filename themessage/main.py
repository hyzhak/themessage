import click
import logging
import themessage
from themessage import markdown, medium_integration, medium_auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')


@click.group()
@click.version_option(version=themessage.__version__)
def cli():
    pass


@cli.command()
def login():
    token = medium_auth.request_token()
    click.echo(token)


@cli.command()
@click.option('--token',
              default=None,
              envvar='MEDIUM_AUTH_TOKEN',
              help='User token. Use command --auth to get it',
              )
@click.argument('ARTICLE', default=None, type=click.File())
def publish(token, article):
    # publish article
    click.echo('publish article')

    # If we don't have token, ask user to authorize
    if not token:
        token = medium_auth.request_token()
        # TODO: store user's token and restore it next time when app will run

    # with open('examples/article.md') as f:
    # with open(article) as f:
    md = article.read()
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
