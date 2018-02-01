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


def send_request_for_token(user_id=None):
    """
    make request for token
    :return:
    """
    user_id = user_id or str(uuid.uuid1())

    auth_url = medium_integration.get_url(
        user_id=user_id,
    )
    return (user_id, auth_url)


def wait_for_token(user_id):
    """
    wait for token for user_id

    :param user_id:
    :return:
    """
    code = _wait_auth_code(user_id)
    # change a code to the token
    return medium_integration.authorize(code)
