import click
import logging
import themessage
from themessage import markdown, medium_integration, medium_auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')


def __request_token():
    click.echo('We are going to get user auth token. '
               'To be able to publish article on Medium')
    user_id, auth_url = medium_auth.send_request_for_token()
    click.echo(f'[!] tap here to login: {auth_url}')
    token = medium_auth.wait_for_token(user_id)
    click.echo(f'[!] we got token: {token}')
    return token


@click.group()
@click.version_option(version=themessage.__version__)
def main():
    pass


@main.command()
def login():
    """
    Request user's token
    """
    __request_token()


@main.command()
@click.option('--token',
              default=None,
              envvar='MEDIUM_AUTH_TOKEN',
              help='User token. Use command login to get it',
              )
@click.argument('article',
                required=False,
                envvar='THEMESSAGE_ARTICLE_FILE',
                type=click.File(),
                )
def publish(token, article):
    # help='path to the article'
    """
    Publish article to the Medium
    """
    # publish article
    click.echo(f'We are going to publish article {article.name}')

    # If we don't have token, ask user to authorize
    if not token:
        token = __request_token()
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
    click.echo(f'Article available on {res["url"]}')
