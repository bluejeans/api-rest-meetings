# coding: utf-8

"""
    BlueJeans onVideo REST API

    _Video That Works Where You Do, from the world's leader in cloud video communication._ # Authentication Each API request that is sent to BlueJeans requires an access token, which is obtained through the BlueJeans Authentication API. There are several methods (grant types) for obtaining an access token, which follow the OAuth2.0 specification. ## Grant Types * Authorization Code Grant – This grant type is used in an authentication flow commonly referred to as \"three-legged OAuth\". The user authenticates via a BlueJeans page, which provides an authorization code. This code, along with a few other elements, can be used to obtain an access code. * Password Credentials Grant – This grant type is used in a two-legged OAuth flow. Username and password are sent to retrieve an access code. * Client Credentials Grant – This grant type is used in a two-legged OAuth flow.  ## Access & Permissions The access level that is associated with each access token is referred to as the scope. There are three basic levels of access that BlueJeans allows, which affect the level of scope.  Three access levels exist within the Blue Jeans service today. * Meeting-level – Authentication takes place using a meeting ID and passcode, and the scope is limited to APIs that relate to the individual meeting. * User-level – Authentication either takes place via three-legged OAuth, or else a direct authorization token request containing a username or password. Access level depends on the requested scope permissions. * App-level – An application is provisioned either by BlueJeans personnel, or within the BlueJeans Enterprise Admin interface. When provisioning an app, a client key and secret are provided, which is then used to obtain an access token, via the BlueJeans Authentication API. The scope that is associated with the token will provide access to an entire enterprise and all of its users.  All endpoints in this document that require Enterprise Admin access will be marked as such. ## Testing In order to make effective use of this page, you will first use one of the authentication methods to obtain an access token. Once the token is given, use the Authenticate button up in the header to store the token. Each BlueJeans API called after that will use the access token provided. 

    OpenAPI spec version: 1.0.0
    Contact: brandon@bluejeans.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class GrantMeetingScopeMeeting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, leader_id=None, meeting_numeric_id=None, meeting_uri=None, is_moderator=None, endpoint_uri_set=None, meeting_id=None):
        """
        GrantMeetingScopeMeeting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'leader_id': 'int',
            'meeting_numeric_id': 'str',
            'meeting_uri': 'str',
            'is_moderator': 'bool',
            'endpoint_uri_set': 'list[object]',
            'meeting_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'leader_id': 'leaderId',
            'meeting_numeric_id': 'meetingNumericId',
            'meeting_uri': 'meetingUri',
            'is_moderator': 'isModerator',
            'endpoint_uri_set': 'endpointUriSet',
            'meeting_id': 'meetingId'
        }

        self._id = id
        self._leader_id = leader_id
        self._meeting_numeric_id = meeting_numeric_id
        self._meeting_uri = meeting_uri
        self._is_moderator = is_moderator
        self._endpoint_uri_set = endpoint_uri_set
        self._meeting_id = meeting_id

    @property
    def id(self):
        """
        Gets the id of this GrantMeetingScopeMeeting.


        :return: The id of this GrantMeetingScopeMeeting.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GrantMeetingScopeMeeting.


        :param id: The id of this GrantMeetingScopeMeeting.
        :type: int
        """

        self._id = id

    @property
    def leader_id(self):
        """
        Gets the leader_id of this GrantMeetingScopeMeeting.


        :return: The leader_id of this GrantMeetingScopeMeeting.
        :rtype: int
        """
        return self._leader_id

    @leader_id.setter
    def leader_id(self, leader_id):
        """
        Sets the leader_id of this GrantMeetingScopeMeeting.


        :param leader_id: The leader_id of this GrantMeetingScopeMeeting.
        :type: int
        """

        self._leader_id = leader_id

    @property
    def meeting_numeric_id(self):
        """
        Gets the meeting_numeric_id of this GrantMeetingScopeMeeting.


        :return: The meeting_numeric_id of this GrantMeetingScopeMeeting.
        :rtype: str
        """
        return self._meeting_numeric_id

    @meeting_numeric_id.setter
    def meeting_numeric_id(self, meeting_numeric_id):
        """
        Sets the meeting_numeric_id of this GrantMeetingScopeMeeting.


        :param meeting_numeric_id: The meeting_numeric_id of this GrantMeetingScopeMeeting.
        :type: str
        """

        self._meeting_numeric_id = meeting_numeric_id

    @property
    def meeting_uri(self):
        """
        Gets the meeting_uri of this GrantMeetingScopeMeeting.


        :return: The meeting_uri of this GrantMeetingScopeMeeting.
        :rtype: str
        """
        return self._meeting_uri

    @meeting_uri.setter
    def meeting_uri(self, meeting_uri):
        """
        Sets the meeting_uri of this GrantMeetingScopeMeeting.


        :param meeting_uri: The meeting_uri of this GrantMeetingScopeMeeting.
        :type: str
        """

        self._meeting_uri = meeting_uri

    @property
    def is_moderator(self):
        """
        Gets the is_moderator of this GrantMeetingScopeMeeting.


        :return: The is_moderator of this GrantMeetingScopeMeeting.
        :rtype: bool
        """
        return self._is_moderator

    @is_moderator.setter
    def is_moderator(self, is_moderator):
        """
        Sets the is_moderator of this GrantMeetingScopeMeeting.


        :param is_moderator: The is_moderator of this GrantMeetingScopeMeeting.
        :type: bool
        """

        self._is_moderator = is_moderator

    @property
    def endpoint_uri_set(self):
        """
        Gets the endpoint_uri_set of this GrantMeetingScopeMeeting.


        :return: The endpoint_uri_set of this GrantMeetingScopeMeeting.
        :rtype: list[object]
        """
        return self._endpoint_uri_set

    @endpoint_uri_set.setter
    def endpoint_uri_set(self, endpoint_uri_set):
        """
        Sets the endpoint_uri_set of this GrantMeetingScopeMeeting.


        :param endpoint_uri_set: The endpoint_uri_set of this GrantMeetingScopeMeeting.
        :type: list[object]
        """

        self._endpoint_uri_set = endpoint_uri_set

    @property
    def meeting_id(self):
        """
        Gets the meeting_id of this GrantMeetingScopeMeeting.


        :return: The meeting_id of this GrantMeetingScopeMeeting.
        :rtype: str
        """
        return self._meeting_id

    @meeting_id.setter
    def meeting_id(self, meeting_id):
        """
        Sets the meeting_id of this GrantMeetingScopeMeeting.


        :param meeting_id: The meeting_id of this GrantMeetingScopeMeeting.
        :type: str
        """

        self._meeting_id = meeting_id

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
