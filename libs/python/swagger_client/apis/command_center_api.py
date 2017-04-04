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

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CommandCenterApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def v1_enterprise_enterprise_id_indigo_meetings_get(self, enterprise_id, **kwargs):
        """
        List Past Meetings by Enterprise
        This endpoint lists completed meetings by enterprise.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_enterprise_enterprise_id_indigo_meetings_get(enterprise_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int enterprise_id: The ID of the enterprise of interest. This value is an integer which can be retrieved for the current user via the Get Enterprise Profile endpoint. (required)
        :param int offset: Page Number
        :param int limit: Per page
        :param str filter: URL-encoded JSON string
        :return: Meeting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_enterprise_enterprise_id_indigo_meetings_get_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.v1_enterprise_enterprise_id_indigo_meetings_get_with_http_info(enterprise_id, **kwargs)
            return data

    def v1_enterprise_enterprise_id_indigo_meetings_get_with_http_info(self, enterprise_id, **kwargs):
        """
        List Past Meetings by Enterprise
        This endpoint lists completed meetings by enterprise.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_enterprise_enterprise_id_indigo_meetings_get_with_http_info(enterprise_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int enterprise_id: The ID of the enterprise of interest. This value is an integer which can be retrieved for the current user via the Get Enterprise Profile endpoint. (required)
        :param int offset: Page Number
        :param int limit: Per page
        :param str filter: URL-encoded JSON string
        :return: Meeting
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'offset', 'limit', 'filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_enterprise_enterprise_id_indigo_meetings_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params) or (params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `v1_enterprise_enterprise_id_indigo_meetings_get`")

        resource_path = '/v1/enterprise/{enterprise_id}/indigo/meetings'.replace('{format}', 'json')
        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = {}
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'filter' in params:
            query_params['filter'] = params['filter']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Meeting',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_enterprise_enterprise_id_indigo_meetings_live_get(self, enterprise_id, **kwargs):
        """
        Live Meetings Summary by Enterprise
        This endpoint lists meetings in progress by enterprise.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_enterprise_enterprise_id_indigo_meetings_live_get(enterprise_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int enterprise_id: The ID of the enterprise of interest. This value is an integer which can be retrieved for the current user via the Get Enterprise Profile endpoint. (required)
        :return: Meeting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_enterprise_enterprise_id_indigo_meetings_live_get_with_http_info(enterprise_id, **kwargs)
        else:
            (data) = self.v1_enterprise_enterprise_id_indigo_meetings_live_get_with_http_info(enterprise_id, **kwargs)
            return data

    def v1_enterprise_enterprise_id_indigo_meetings_live_get_with_http_info(self, enterprise_id, **kwargs):
        """
        Live Meetings Summary by Enterprise
        This endpoint lists meetings in progress by enterprise.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_enterprise_enterprise_id_indigo_meetings_live_get_with_http_info(enterprise_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int enterprise_id: The ID of the enterprise of interest. This value is an integer which can be retrieved for the current user via the Get Enterprise Profile endpoint. (required)
        :return: Meeting
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_enterprise_enterprise_id_indigo_meetings_live_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params) or (params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `v1_enterprise_enterprise_id_indigo_meetings_live_get`")

        resource_path = '/v1/enterprise/{enterprise_id}/indigo/meetings/live'.replace('{format}', 'json')
        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Meeting',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get(self, enterprise_id, meeting_guid, **kwargs):
        """
        List Live Meeting Endpoints by Enterprise
        This endpoint lists endpoints for a given meeting in progress.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get(enterprise_id, meeting_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int enterprise_id: The ID of the enterprise of interest. This value is an integer which can be retrieved for the current user via the Get Enterprise Profile endpoint. (required)
        :param str meeting_guid: The globally unique identifier (GUID) of the meeting of interest. This value is a string which contains the numeric meeting id, followed by a colon, followed by a 128-bit integer number formatted as 5 alphanumeric segments separated by dashes. Since a given numeric meeting ID can have multiple instantiations over time, the GUID helps identify the instance of interest. (required)
        :return: Meeting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get_with_http_info(enterprise_id, meeting_guid, **kwargs)
        else:
            (data) = self.v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get_with_http_info(enterprise_id, meeting_guid, **kwargs)
            return data

    def v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get_with_http_info(self, enterprise_id, meeting_guid, **kwargs):
        """
        List Live Meeting Endpoints by Enterprise
        This endpoint lists endpoints for a given meeting in progress.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get_with_http_info(enterprise_id, meeting_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int enterprise_id: The ID of the enterprise of interest. This value is an integer which can be retrieved for the current user via the Get Enterprise Profile endpoint. (required)
        :param str meeting_guid: The globally unique identifier (GUID) of the meeting of interest. This value is a string which contains the numeric meeting id, followed by a colon, followed by a 128-bit integer number formatted as 5 alphanumeric segments separated by dashes. Since a given numeric meeting ID can have multiple instantiations over time, the GUID helps identify the instance of interest. (required)
        :return: Meeting
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'meeting_guid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params) or (params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get`")
        # verify the required parameter 'meeting_guid' is set
        if ('meeting_guid' not in params) or (params['meeting_guid'] is None):
            raise ValueError("Missing the required parameter `meeting_guid` when calling `v1_enterprise_enterprise_id_indigo_meetings_live_meeting_guid_endpoints_get`")

        resource_path = '/v1/enterprise/{enterprise_id}/indigo/meetings/live/{meeting_guid}/endpoints/'.replace('{format}', 'json')
        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'meeting_guid' in params:
            path_params['meeting_guid'] = params['meeting_guid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Meeting',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get(self, enterprise_id, meeting_guid, **kwargs):
        """
        List Meeting Endpoints & Stats by Enterprise
        This endpoint lists meeting endpoints for completed meetings by enterprise.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get(enterprise_id, meeting_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int enterprise_id: The ID of the enterprise of interest. This value is an integer which can be retrieved for the current user via the Get Enterprise Profile endpoint. (required)
        :param str meeting_guid: The globally unique identifier (GUID) of the meeting of interest. This value is a string which contains the numeric meeting id, followed by a colon, followed by a 128-bit integer number formatted as 5 alphanumeric segments separated by dashes. Since a given numeric meeting ID can have multiple instantiations over time, the GUID helps identify the instance of interest. (required)
        :param bool include_endpoints: Option to include detailed data on endpoints
        :return: MeetingIndigo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get_with_http_info(enterprise_id, meeting_guid, **kwargs)
        else:
            (data) = self.v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get_with_http_info(enterprise_id, meeting_guid, **kwargs)
            return data

    def v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get_with_http_info(self, enterprise_id, meeting_guid, **kwargs):
        """
        List Meeting Endpoints & Stats by Enterprise
        This endpoint lists meeting endpoints for completed meetings by enterprise.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get_with_http_info(enterprise_id, meeting_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int enterprise_id: The ID of the enterprise of interest. This value is an integer which can be retrieved for the current user via the Get Enterprise Profile endpoint. (required)
        :param str meeting_guid: The globally unique identifier (GUID) of the meeting of interest. This value is a string which contains the numeric meeting id, followed by a colon, followed by a 128-bit integer number formatted as 5 alphanumeric segments separated by dashes. Since a given numeric meeting ID can have multiple instantiations over time, the GUID helps identify the instance of interest. (required)
        :param bool include_endpoints: Option to include detailed data on endpoints
        :return: MeetingIndigo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id', 'meeting_guid', 'include_endpoints']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params) or (params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get`")
        # verify the required parameter 'meeting_guid' is set
        if ('meeting_guid' not in params) or (params['meeting_guid'] is None):
            raise ValueError("Missing the required parameter `meeting_guid` when calling `v1_enterprise_enterprise_id_indigo_meetings_meeting_guid_get`")

        resource_path = '/v1/enterprise/{enterprise_id}/indigo/meetings/{meeting_guid}'.replace('{format}', 'json')
        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']
        if 'meeting_guid' in params:
            path_params['meeting_guid'] = params['meeting_guid']

        query_params = {}
        if 'include_endpoints' in params:
            query_params['includeEndpoints'] = params['include_endpoints']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MeetingIndigo',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_user_user_id_indigo_meetings_get(self, user_id, **kwargs):
        """
        List Past Meetings by User
        This endpoint lists completed meetings by user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_user_id_indigo_meetings_get(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: The ID of the user of interest. This value is an integer which can be retrieved for the current user via the Get User Account Details endpoint. (required)
        :return: Meeting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_user_user_id_indigo_meetings_get_with_http_info(user_id, **kwargs)
        else:
            (data) = self.v1_user_user_id_indigo_meetings_get_with_http_info(user_id, **kwargs)
            return data

    def v1_user_user_id_indigo_meetings_get_with_http_info(self, user_id, **kwargs):
        """
        List Past Meetings by User
        This endpoint lists completed meetings by user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_user_id_indigo_meetings_get_with_http_info(user_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: The ID of the user of interest. This value is an integer which can be retrieved for the current user via the Get User Account Details endpoint. (required)
        :return: Meeting
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_user_user_id_indigo_meetings_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `v1_user_user_id_indigo_meetings_get`")

        resource_path = '/v1/user/{user_id}/indigo/meetings'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Meeting',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def v1_user_user_id_indigo_meetings_meeting_guid_get(self, user_id, meeting_guid, **kwargs):
        """
        List Meeting Endpoints & Stats by User
        This endpoint lists meeting endpoints for completed meetings by user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_user_id_indigo_meetings_meeting_guid_get(user_id, meeting_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: The ID of the user of interest. This value is an integer which can be retrieved for the current user via the Get User Account Details endpoint. (required)
        :param str meeting_guid: The globally unique identifier (GUID) of the meeting of interest. This value is a string which contains the numeric meeting id, followed by a colon, followed by a 128-bit integer number formatted as 5 alphanumeric segments separated by dashes. Since a given numeric meeting ID can have multiple instantiations over time, the GUID helps identify the instance of interest. (required)
        :return: MeetingIndigo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.v1_user_user_id_indigo_meetings_meeting_guid_get_with_http_info(user_id, meeting_guid, **kwargs)
        else:
            (data) = self.v1_user_user_id_indigo_meetings_meeting_guid_get_with_http_info(user_id, meeting_guid, **kwargs)
            return data

    def v1_user_user_id_indigo_meetings_meeting_guid_get_with_http_info(self, user_id, meeting_guid, **kwargs):
        """
        List Meeting Endpoints & Stats by User
        This endpoint lists meeting endpoints for completed meetings by user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.v1_user_user_id_indigo_meetings_meeting_guid_get_with_http_info(user_id, meeting_guid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int user_id: The ID of the user of interest. This value is an integer which can be retrieved for the current user via the Get User Account Details endpoint. (required)
        :param str meeting_guid: The globally unique identifier (GUID) of the meeting of interest. This value is a string which contains the numeric meeting id, followed by a colon, followed by a 128-bit integer number formatted as 5 alphanumeric segments separated by dashes. Since a given numeric meeting ID can have multiple instantiations over time, the GUID helps identify the instance of interest. (required)
        :return: MeetingIndigo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'meeting_guid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_user_user_id_indigo_meetings_meeting_guid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `v1_user_user_id_indigo_meetings_meeting_guid_get`")
        # verify the required parameter 'meeting_guid' is set
        if ('meeting_guid' not in params) or (params['meeting_guid'] is None):
            raise ValueError("Missing the required parameter `meeting_guid` when calling `v1_user_user_id_indigo_meetings_meeting_guid_get`")

        resource_path = '/v1/user/{user_id}/indigo/meetings/{meeting_guid}'.replace('{format}', 'json')
        path_params = {}
        if 'user_id' in params:
            path_params['user_id'] = params['user_id']
        if 'meeting_guid' in params:
            path_params['meeting_guid'] = params['meeting_guid']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['access_token']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='MeetingIndigo',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))