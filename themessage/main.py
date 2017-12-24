import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('main')

import os
import requests
from themessage import medium_integration


def main():
    # publish article
    # could use this example https://github.com/Medium/medium-sdk-python

    # If we don't have token, ask user to authorize
    token = None
    if not token:
        # TODO: should generate uniq user id
        user_id = 'qwerty'
        auth_url = medium_integration.get_url(
            user_id=user_id,
        )

        logger.info(f'[!] tap here: {auth_url}')

        # TODO: request code from server and wait
        # change a code to the token
        # once we get token store it
        query_url = os.environ['MEDIUM_APP_AUTH_CODE_SUBSCRIBE_URL'].format(
            user_id=user_id,
        )
        logger.info(f'start listen {query_url}')
        res = requests.get(query_url)
        logger.info(f'get result {res.text}')
        lines = res.text.strip().splitlines()
        if len(lines) == 0:
            raise Exception(f'do not receive code')
        code = lines[-1].replace('data:', '').strip()
        logger.info(f'receive code {code}')
        token = medium_integration.authorize(code)
        logger.info(f'receive token {token}')
        # TODO: store user's token
        # publish article by user token


if __name__ == '__main__':
    logger.info('just before run main')
    main()
