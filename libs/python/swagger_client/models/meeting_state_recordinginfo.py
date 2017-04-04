# coding: utf-8

"""
    BlueJeans onVideo REST API

    _Video That Works Where You Do._  This site provides developers access to API's from BlueJean's onVideo meeting service.  From here you will be able to make actual API calls to manage User Accounts, Meetings, and Recordings.  Also, you can pull analytical data as well retrieve current state information.  With these API's  you should be able to quickly integrate **BlueJeans** video into your applications.     # Authentication All API transactions (excluding Authentication) require an access token per **OAuth standards**.  BlueJeans provides multiple methods for obtaining an access token.  Additionally there are diffferent scopes of token access. ## Grant Types Bluejeans provides 3 different methods for users to Authenticate.  Successful authentication allows BlueJeans to grant an access token to the user. * Authorization Code Grant – Authenticate via a BlueJeans page, and receive an authorization code. Submit authorization with other tokens and receive an access code. (\"three-legged OAuth\") * Password Credentials Grant – Authenticate with a Username and password and receives an access code. (\"two-legged OAuth\"); * Client Credentials Grant – Similar to Password Grant (\"two-legged OAuth\").  ## Access & Permissions BlueJeans defines 3 levels of API access into the system.  When an access token is granted, it carries one of these 3 levels.  The scope of system functionality depends upon the token's access level. * Meeting-level – scope of APIs is limited to individual meetings. * User-level – scope depends on the requested permissions. * App-level – provisioned either by BlueJeans personnel, or the BlueJeans Enterprise Admin, an app, is issued a client key and secret key. These tokens then are used by the BlueJeans Authentication API to receive the token. The token's scope provides access to the entire enterprise and all of its users.  All endpoints in this document that require **Enterprise Admin** access will be marked as such. # Getting Started Before you start using the API's on this site, you must first have a BlueJeans account.  With your BlueJean credentials, use on of the Authentication methods to obtain an access token. - Click on the Authorize button at the top of page - Enter your access token in the field marked \"api_key\" Now the web site will automatically include your access token on all API calls you make. 

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


class MeetingStateRecordinginfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, content_status=None, recording_start_time=None, active=None, recorded=None):
        """
        MeetingStateRecordinginfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content_status': 'str',
            'recording_start_time': 'int',
            'active': 'bool',
            'recorded': 'bool'
        }

        self.attribute_map = {
            'content_status': 'contentStatus',
            'recording_start_time': 'recordingStartTime',
            'active': 'active',
            'recorded': 'recorded'
        }

        self._content_status = content_status
        self._recording_start_time = recording_start_time
        self._active = active
        self._recorded = recorded

    @property
    def content_status(self):
        """
        Gets the content_status of this MeetingStateRecordinginfo.


        :return: The content_status of this MeetingStateRecordinginfo.
        :rtype: str
        """
        return self._content_status

    @content_status.setter
    def content_status(self, content_status):
        """
        Sets the content_status of this MeetingStateRecordinginfo.


        :param content_status: The content_status of this MeetingStateRecordinginfo.
        :type: str
        """

        self._content_status = content_status

    @property
    def recording_start_time(self):
        """
        Gets the recording_start_time of this MeetingStateRecordinginfo.


        :return: The recording_start_time of this MeetingStateRecordinginfo.
        :rtype: int
        """
        return self._recording_start_time

    @recording_start_time.setter
    def recording_start_time(self, recording_start_time):
        """
        Sets the recording_start_time of this MeetingStateRecordinginfo.


        :param recording_start_time: The recording_start_time of this MeetingStateRecordinginfo.
        :type: int
        """

        self._recording_start_time = recording_start_time

    @property
    def active(self):
        """
        Gets the active of this MeetingStateRecordinginfo.


        :return: The active of this MeetingStateRecordinginfo.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this MeetingStateRecordinginfo.


        :param active: The active of this MeetingStateRecordinginfo.
        :type: bool
        """

        self._active = active

    @property
    def recorded(self):
        """
        Gets the recorded of this MeetingStateRecordinginfo.


        :return: The recorded of this MeetingStateRecordinginfo.
        :rtype: bool
        """
        return self._recorded

    @recorded.setter
    def recorded(self, recorded):
        """
        Sets the recorded of this MeetingStateRecordinginfo.


        :param recorded: The recorded of this MeetingStateRecordinginfo.
        :type: bool
        """

        self._recorded = recorded

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