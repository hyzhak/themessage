import logging

logger = logging.getLogger(__name__)

import os
import requests
from themessage import medium_integration
import uuid


def _wait_auth_code(user_id):
    """
    request code from server and wait

    :param user_id:
    :return:
    """
    query_url = os.environ['MEDIUM_APP_AUTH_CODE_SUBSCRIBE_URL'].format(
        user_id=user_id,
    )
    logger.debug(f'start listen {query_url}')
    res = requests.get(query_url)
    logger.debug(f'get result {res.text}')
    lines = res.text.strip().splitlines()
    if len(lines) == 0:
        raise Exception(f'do not receive code')
    code = lines[-1].replace('data:', '').strip()
    logger.debug(f'receive code {code}')
    return code


def request_token():
    user_id = str(uuid.uuid1())

    auth_url = medium_integration.get_url(
        user_id=user_id,
    )
    logger.info(f'[!] tap here: {auth_url}')

    code = _wait_auth_code(user_id)

    # change a code to the token
    token = medium_integration.authorize(code)
    logger.debug(f'receive token {token}')
    return token
