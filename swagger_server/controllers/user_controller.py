import connexion
import six
from swagger_server.mycelery import celery
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util

from flask import request,session,stream_with_context

import  threading

@celery.task
def login_get_cd(name):  # noqa: E501
    """User Login

    System User Login # noqa: E501

    :param name: data
    :type name: str

    :rtype: InlineResponse200
    """
    print("start")
    msg='none'
    try:
        session['click'] += 1
        print(session.get('click'))
        msg = {'result': '第{}次点击'.format(session.get('click'))}
    except:
        pass


    return msg
    #     session['click'] = click + 1
    #     yield session
    #     print('还有：{}s'.format(click))
    #     yield msg
    #
    #     # print('还剩下:{}s'.format(600-click))
    # rsp=Response(stream_with_context(generate()))
    # return rsp





@celery.task
def login_get_jzh(name):  # noqa: E501
    """User Login

     System UserLogin # noqa: E501

    :param name: data
    :type name: str

    :rtype: InlineResponse200
    """

    name_list=[]
    def work(name,i):
        print(i)
        name_list.append(name+str(i))
        return
    work_list=[]
    for i in range(5):
        t = threading.Thread(target=work,args=(name,i,))
        t.start()
        work_list.append(t)
    for item in work_list:
        item.join()

    msg={'result':name_list}
    return msg