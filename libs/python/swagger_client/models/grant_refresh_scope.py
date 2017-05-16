# coding: utf-8

"""
    BlueJeans onVideo REST API

    _Video That Works Where You Do._  This site provides developers access to API's from BlueJean's onVideo meeting service.  From here you will be able to make actual API calls to manage User Accounts, Meetings, and Recordings.  Also, you can pull analytical data as well retrieve current state information.  With these API's  you should be able to quickly integrate **BlueJeans** video into your applications.     # Authentication All API transactions (excluding Authentication) require an access token per **OAuth standards**.  BlueJeans provides multiple methods for obtaining an access token.  Additionally there are diffferent scopes of token access. ## Grant Types Bluejeans provides 4 different methods for users to Authenticate.  Successful authentication allows BlueJeans to grant an access token to perform operations. * Password Credentials Grant – Authenticate with a username and password and receive an access token with user level permission. Known as two-legged OAuth. * Meeting Credentials Grant – Authenticate with a meeting ID and meeting passcode and receive an access token with meeting level permission. Known as two-legged OAuth. * Client Credentials Grant –  Authenticate with a client ID and client secret and receive an access token with enterprise level permission. Known as two-legged OAuth. * Authorization Code Grant – After creating a developer application, users witll authenticate via a BlueJeans page, and receive an authorization code. Submit authorization with other tokens and receive an access token. Known as three-legged OAuth. ## Access & Permissions BlueJeans defines 3 levels of API access into the system.  When an access token is granted, it carries one of these 3 levels.  The scope of system functionality depends upon the token's access level. * Meeting-level – Scope of APIs is limited to individual meetings. * User-level – Scope depends on the requested permissions. * App-level – provisioned either by BlueJeans personnel, or the BlueJeans Enterprise Admin, an app, is issued a client key and secret key. These tokens then are used by the BlueJeans Authentication API to receive the token. The token's scope provides access to the entire enterprise and all of its users. All endpoints in this document that require **Enterprise Admin** access will be marked as such. # Getting Started Before you start using the API's on this site, you must first have a BlueJeans account.  With your BlueJean credentials, use one of the Authentication methods to obtain an access token. - Click on the Authorize button at the top of page - Enter your access token in the field marked \"api_key\" Now the web site will automatically include your access token on all API calls you make. 

    OpenAPI spec version: 1.0.0
    Contact: brandon@bluejeans.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GrantRefreshScope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, user=None, app_permissions=None, partition_name=None, partition=None, bearer_permissions=None):
        """
        GrantRefreshScope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'user': 'int',
            'app_permissions': 'list[GrantCodeScopeAppPermissions]',
            'partition_name': 'str',
            'partition': 'Partition',
            'bearer_permissions': 'str'
        }

        self.attribute_map = {
            'user': 'user',
            'app_permissions': 'appPermissions',
            'partition_name': 'partitionName',
            'partition': 'partition',
            'bearer_permissions': 'bearerPermissions'
        }

        self._user = user
        self._app_permissions = app_permissions
        self._partition_name = partition_name
        self._partition = partition
        self._bearer_permissions = bearer_permissions

    @property
    def user(self):
        """
        Gets the user of this GrantRefreshScope.
        The ID of your user.

        :return: The user of this GrantRefreshScope.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this GrantRefreshScope.
        The ID of your user.

        :param user: The user of this GrantRefreshScope.
        :type: int
        """

        self._user = user

    @property
    def app_permissions(self):
        """
        Gets the app_permissions of this GrantRefreshScope.

        :return: The app_permissions of this GrantRefreshScope.
        :rtype: list[GrantCodeScopeAppPermissions]
        """
        return self._app_permissions

    @app_permissions.setter
    def app_permissions(self, app_permissions):
        """
        Sets the app_permissions of this GrantRefreshScope.

        :param app_permissions: The app_permissions of this GrantRefreshScope.
        :type: list[GrantCodeScopeAppPermissions]
        """

        self._app_permissions = app_permissions

    @property
    def partition_name(self):
        """
        Gets the partition_name of this GrantRefreshScope.
        The name of the partition you are on.

        :return: The partition_name of this GrantRefreshScope.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        """
        Sets the partition_name of this GrantRefreshScope.
        The name of the partition you are on.

        :param partition_name: The partition_name of this GrantRefreshScope.
        :type: str
        """

        self._partition_name = partition_name

    @property
    def partition(self):
        """
        Gets the partition of this GrantRefreshScope.

        :return: The partition of this GrantRefreshScope.
        :rtype: Partition
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """
        Sets the partition of this GrantRefreshScope.

        :param partition: The partition of this GrantRefreshScope.
        :type: Partition
        """

        self._partition = partition

    @property
    def bearer_permissions(self):
        """
        Gets the bearer_permissions of this GrantRefreshScope.
        Comma-delimited list of scopes authorized by this token.

        :return: The bearer_permissions of this GrantRefreshScope.
        :rtype: str
        """
        return self._bearer_permissions

    @bearer_permissions.setter
    def bearer_permissions(self, bearer_permissions):
        """
        Sets the bearer_permissions of this GrantRefreshScope.
        Comma-delimited list of scopes authorized by this token.

        :param bearer_permissions: The bearer_permissions of this GrantRefreshScope.
        :type: str
        """

        self._bearer_permissions = bearer_permissions

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GrantRefreshScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other