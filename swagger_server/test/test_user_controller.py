# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_login_get_cd(self):
        """Test case for login_get_cd

        User Login
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/login_jzh',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_get_jzh(self):
        """Test case for login_get_jzh

        User Login
        """
        query_string = [('name', 'name_example')]
        response = self.client.open(
            '/v1/login_cd',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
