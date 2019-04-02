import connexion
import six
from swagger_server.celery import celery
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util

@celery.task
def login_get_cd(name):  # noqa: E501
    """User Login

    System User Login # noqa: E501

    :param name: data
    :type name: str

    :rtype: InlineResponse200
    """
    msg={'result':name}
    return msg

@celery.task
def login_get_jzh(name):  # noqa: E501
    """User Login

    System User Login # noqa: E501

    :param name: data
    :type name: str

    :rtype: InlineResponse200
    """
    import time
    time.sleep(10)
    msg={'result':name}
    return msg
