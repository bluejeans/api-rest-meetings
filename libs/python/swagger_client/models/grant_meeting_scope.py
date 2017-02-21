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


class GrantMeetingScope(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, meeting=None, partition_name=None, partition=None):
        """
        GrantMeetingScope - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'meeting': 'GrantMeetingScopeMeeting',
            'partition_name': 'str',
            'partition': 'Partition'
        }

        self.attribute_map = {
            'meeting': 'meeting',
            'partition_name': 'partitionName',
            'partition': 'partition'
        }

        self._meeting = meeting
        self._partition_name = partition_name
        self._partition = partition

    @property
    def meeting(self):
        """
        Gets the meeting of this GrantMeetingScope.


        :return: The meeting of this GrantMeetingScope.
        :rtype: GrantMeetingScopeMeeting
        """
        return self._meeting

    @meeting.setter
    def meeting(self, meeting):
        """
        Sets the meeting of this GrantMeetingScope.


        :param meeting: The meeting of this GrantMeetingScope.
        :type: GrantMeetingScopeMeeting
        """

        self._meeting = meeting

    @property
    def partition_name(self):
        """
        Gets the partition_name of this GrantMeetingScope.
        The name of the partition you are on.

        :return: The partition_name of this GrantMeetingScope.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        """
        Sets the partition_name of this GrantMeetingScope.
        The name of the partition you are on.

        :param partition_name: The partition_name of this GrantMeetingScope.
        :type: str
        """

        self._partition_name = partition_name

    @property
    def partition(self):
        """
        Gets the partition of this GrantMeetingScope.


        :return: The partition of this GrantMeetingScope.
        :rtype: Partition
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """
        Sets the partition of this GrantMeetingScope.


        :param partition: The partition of this GrantMeetingScope.
        :type: Partition
        """

        self._partition = partition

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
