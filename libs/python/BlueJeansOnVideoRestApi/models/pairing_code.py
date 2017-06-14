# coding: utf-8

"""
    BlueJeans onVideo REST API

     # Video That Works Where You Do. This site provides developers access to API's from BlueJean's onVideo meeting service.  From here you will be able to make actual API calls to manage User Accounts, Meetings, and Recordings.  Also, you can pull analytical data and current state information.  With these API's  you should be able to quickly integrate **BlueJeans** video administration into your applications.     ## Getting Started Before you start using BlueJeans' API's, you must first have a BlueJeans account enabled for API Access.  Contact [BlueJeans Support](mailto:Support@BlueJeans.com) for assistance.  <br /><br />Once you have an account, you may start writing application code to authenticate and make API calls.  *Alternatively*, you can use this developer site to test the BlueJeans' API's and develop a level of familiarity before you write production code.  <br /> ### To Make API Calls from This Site If you want to use this developer site to try various BlueJeans' API's, here are the steps required to authenticate and enable your Developer Session to place API calls. 1. Choose Method for Authenticating       * Click on the desired Authentication method from below.      * Click on the **Try It Out** button. 1. Make Authentication request      * Follow API's instructions and input the API parameters.      * Click on the blue **Execute** button.      * If successful, the API returns with JSON data containing a field called **access_token**.  Copy/save this value. 1. Authorize BlueJeans Developer Session.      * Click on the green **Authorize button**.       * The site will show you a pop-up window for authorization.      * Enter your access token in the field named **api_key**      * Click on the **Authorize** button  Your current BlueJeans developer session is now authenticated and ready to place API calls.  The web site will automatically include your access token on any API calls you make.  ## About onVideo Authentication All API transactions (excluding Authentication) require an access token per **OAuth standards**.  BlueJeans provides multiple methods for obtaining an access token.  Additionally there are diffferent scopes of token access. ### Grant Types Bluejeans provides 4 different methods for users to Authenticate.  Successful authentication allows BlueJeans to grant an access token to perform API operations. * Password Credentials Grant – Authenticate with a username and password and receive an access token with user level permission. Known as two-legged OAuth. * Meeting Credentials Grant – Authenticate with a meeting ID and meeting passcode and receive an access token with meeting level permission. Known as two-legged OAuth. * Client Credentials Grant –  Authenticate with a client ID and client secret and receive an access token with enterprise level permission. Known as two-legged OAuth. * Authorization Code Grant – Authentication for your developer's application occurs through a redirection to a BlueJeans authentication page. The application receives an authorization code to be submitted, along with other tokens, to receive an access token. Known as three-legged OAuth. For more information please refer to the [OAuth specification](https://oauth.net/). ### Access & Permissions BlueJeans defines 3 levels of API access into the system.  When an access token is granted, it carries one of these 3 levels.  The scope of system functionality depends upon the token's access level. * Meeting-level – Scope of APIs is limited to individual meetings. * User-level – Scope depends on the requested permissions. * App-level – provisioned either by BlueJeans personnel, or the BlueJeans Enterprise Admin, an app, is issued a client key and secret key. These tokens then are used by the BlueJeans Authentication API to receive the token. The token's scope provides access to the entire enterprise and all of its users. All endpoints in this document that require **Enterprise Admin** access will be marked as such. 

    OpenAPI spec version: 1.0.0
    Contact: brandon@bluejeans.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PairingCode(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, callguid=None, endpoint_guid=None, force_turn=None, pairing_code=None, status=None, status_text=None, turnservers=None, uri=None, seam_endpoint_guid=None, connection_guid=None, endpoint_name=None):
        """
        PairingCode - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'callguid': 'str',
            'endpoint_guid': 'str',
            'force_turn': 'bool',
            'pairing_code': 'str',
            'status': 'int',
            'status_text': 'str',
            'turnservers': 'list[PairingCodeTurnservers]',
            'uri': 'str',
            'seam_endpoint_guid': 'str',
            'connection_guid': 'str',
            'endpoint_name': 'str'
        }

        self.attribute_map = {
            'callguid': 'callguid',
            'endpoint_guid': 'endpointGuid',
            'force_turn': 'forceTURN',
            'pairing_code': 'pairingCode',
            'status': 'status',
            'status_text': 'statusText',
            'turnservers': 'turnservers',
            'uri': 'uri',
            'seam_endpoint_guid': 'seamEndpointGuid',
            'connection_guid': 'connectionGuid',
            'endpoint_name': 'endpointName'
        }

        self._callguid = callguid
        self._endpoint_guid = endpoint_guid
        self._force_turn = force_turn
        self._pairing_code = pairing_code
        self._status = status
        self._status_text = status_text
        self._turnservers = turnservers
        self._uri = uri
        self._seam_endpoint_guid = seam_endpoint_guid
        self._connection_guid = connection_guid
        self._endpoint_name = endpoint_name

    @property
    def callguid(self):
        """
        Gets the callguid of this PairingCode.

        :return: The callguid of this PairingCode.
        :rtype: str
        """
        return self._callguid

    @callguid.setter
    def callguid(self, callguid):
        """
        Sets the callguid of this PairingCode.

        :param callguid: The callguid of this PairingCode.
        :type: str
        """

        self._callguid = callguid

    @property
    def endpoint_guid(self):
        """
        Gets the endpoint_guid of this PairingCode.

        :return: The endpoint_guid of this PairingCode.
        :rtype: str
        """
        return self._endpoint_guid

    @endpoint_guid.setter
    def endpoint_guid(self, endpoint_guid):
        """
        Sets the endpoint_guid of this PairingCode.

        :param endpoint_guid: The endpoint_guid of this PairingCode.
        :type: str
        """

        self._endpoint_guid = endpoint_guid

    @property
    def force_turn(self):
        """
        Gets the force_turn of this PairingCode.

        :return: The force_turn of this PairingCode.
        :rtype: bool
        """
        return self._force_turn

    @force_turn.setter
    def force_turn(self, force_turn):
        """
        Sets the force_turn of this PairingCode.

        :param force_turn: The force_turn of this PairingCode.
        :type: bool
        """

        self._force_turn = force_turn

    @property
    def pairing_code(self):
        """
        Gets the pairing_code of this PairingCode.

        :return: The pairing_code of this PairingCode.
        :rtype: str
        """
        return self._pairing_code

    @pairing_code.setter
    def pairing_code(self, pairing_code):
        """
        Sets the pairing_code of this PairingCode.

        :param pairing_code: The pairing_code of this PairingCode.
        :type: str
        """

        self._pairing_code = pairing_code

    @property
    def status(self):
        """
        Gets the status of this PairingCode.

        :return: The status of this PairingCode.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PairingCode.

        :param status: The status of this PairingCode.
        :type: int
        """

        self._status = status

    @property
    def status_text(self):
        """
        Gets the status_text of this PairingCode.

        :return: The status_text of this PairingCode.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        """
        Sets the status_text of this PairingCode.

        :param status_text: The status_text of this PairingCode.
        :type: str
        """
        allowed_values = ["OK"]
        if status_text not in allowed_values:
            raise ValueError(
                "Invalid value for `status_text` ({0}), must be one of {1}"
                .format(status_text, allowed_values)
            )

        self._status_text = status_text

    @property
    def turnservers(self):
        """
        Gets the turnservers of this PairingCode.

        :return: The turnservers of this PairingCode.
        :rtype: list[PairingCodeTurnservers]
        """
        return self._turnservers

    @turnservers.setter
    def turnservers(self, turnservers):
        """
        Sets the turnservers of this PairingCode.

        :param turnservers: The turnservers of this PairingCode.
        :type: list[PairingCodeTurnservers]
        """

        self._turnservers = turnservers

    @property
    def uri(self):
        """
        Gets the uri of this PairingCode.

        :return: The uri of this PairingCode.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this PairingCode.

        :param uri: The uri of this PairingCode.
        :type: str
        """

        self._uri = uri

    @property
    def seam_endpoint_guid(self):
        """
        Gets the seam_endpoint_guid of this PairingCode.

        :return: The seam_endpoint_guid of this PairingCode.
        :rtype: str
        """
        return self._seam_endpoint_guid

    @seam_endpoint_guid.setter
    def seam_endpoint_guid(self, seam_endpoint_guid):
        """
        Sets the seam_endpoint_guid of this PairingCode.

        :param seam_endpoint_guid: The seam_endpoint_guid of this PairingCode.
        :type: str
        """

        self._seam_endpoint_guid = seam_endpoint_guid

    @property
    def connection_guid(self):
        """
        Gets the connection_guid of this PairingCode.

        :return: The connection_guid of this PairingCode.
        :rtype: str
        """
        return self._connection_guid

    @connection_guid.setter
    def connection_guid(self, connection_guid):
        """
        Sets the connection_guid of this PairingCode.

        :param connection_guid: The connection_guid of this PairingCode.
        :type: str
        """

        self._connection_guid = connection_guid

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this PairingCode.

        :return: The endpoint_name of this PairingCode.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this PairingCode.

        :param endpoint_name: The endpoint_name of this PairingCode.
        :type: str
        """

        self._endpoint_name = endpoint_name

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
        if not isinstance(other, PairingCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
