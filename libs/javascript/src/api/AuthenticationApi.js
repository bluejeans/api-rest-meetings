/**
 * BlueJeans onVideo REST API
 * _Video That Works Where You Do, from the world's leader in cloud video communication._ # Authentication Each API request that is sent to BlueJeans requires an access token, which is obtained through the BlueJeans Authentication API. There are several methods (grant types) for obtaining an access token, which follow the OAuth2.0 specification. ## Grant Types * Authorization Code Grant – This grant type is used in an authentication flow commonly referred to as \"three-legged OAuth\". The user authenticates via a BlueJeans page, which provides an authorization code. This code, along with a few other elements, can be used to obtain an access code. * Password Credentials Grant – This grant type is used in a two-legged OAuth flow. Username and password are sent to retrieve an access code. * Client Credentials Grant – This grant type is used in a two-legged OAuth flow.  ## Access & Permissions The access level that is associated with each access token is referred to as the scope. There are three basic levels of access that BlueJeans allows, which affect the level of scope.  Three access levels exist within the Blue Jeans service today. * Meeting-level – Authentication takes place using a meeting ID and passcode, and the scope is limited to APIs that relate to the individual meeting. * User-level – Authentication either takes place via three-legged OAuth, or else a direct authorization token request containing a username or password. Access level depends on the requested scope permissions. * App-level – An application is provisioned either by BlueJeans personnel, or within the BlueJeans Enterprise Admin interface. When provisioning an app, a client key and secret are provided, which is then used to obtain an access token, via the BlueJeans Authentication API. The scope that is associated with the token will provide access to an entire enterprise and all of its users.  All endpoints in this document that require Enterprise Admin access will be marked as such. ## Testing In order to make effective use of this page, you will first use one of the authentication methods to obtain an access token. Once the token is given, use the Authenticate button up in the header to store the token. Each BlueJeans API called after that will use the access token provided. 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: brandon@bluejeans.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/GrantClient', 'model/GrantTypeClient', 'model/Error', 'model/GrantMeeting', 'model/GrantTypeMeeting', 'model/GrantTypePassword', 'model/GrantPassword'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('../model/GrantClient'), require('../model/GrantTypeClient'), require('../model/Error'), require('../model/GrantMeeting'), require('../model/GrantTypeMeeting'), require('../model/GrantTypePassword'), require('../model/GrantPassword'));
  } else {
    // Browser globals (root is window)
    if (!root.BlueJeansOnVideoRestApi) {
      root.BlueJeansOnVideoRestApi = {};
    }
    root.BlueJeansOnVideoRestApi.AuthenticationApi = factory(root.BlueJeansOnVideoRestApi.ApiClient, root.BlueJeansOnVideoRestApi.GrantClient, root.BlueJeansOnVideoRestApi.GrantTypeClient, root.BlueJeansOnVideoRestApi.Error, root.BlueJeansOnVideoRestApi.GrantMeeting, root.BlueJeansOnVideoRestApi.GrantTypeMeeting, root.BlueJeansOnVideoRestApi.GrantTypePassword, root.BlueJeansOnVideoRestApi.GrantPassword);
  }
}(this, function(ApiClient, GrantClient, GrantTypeClient, Error, GrantMeeting, GrantTypeMeeting, GrantTypePassword, GrantPassword) {
  'use strict';

  /**
   * Authentication service.
   * @module api/AuthenticationApi
   * @version 1.0.0
   */

  /**
   * Constructs a new AuthenticationApi. 
   * @alias module:api/AuthenticationApi
   * @class
   * @param {module:ApiClient} apiClient Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  var exports = function(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;


    /**
     * Callback function to receive the result of the getTokenByClient operation.
     * @callback module:api/AuthenticationApi~getTokenByClientCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GrantClient} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Authentication via Client Grant Type
     * This grant type is commonly used by an app. Client ID and Secret are provisioned within the BlueJeans Enterprise Administration console.
     * @param {module:model/GrantTypeClient} grantTypeClient Contains information about the type of grant you are requesting.
     * @param {module:api/AuthenticationApi~getTokenByClientCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GrantClient}
     */
    this.getTokenByClient = function(grantTypeClient, callback) {
      var postBody = grantTypeClient;

      // verify the required parameter 'grantTypeClient' is set
      if (grantTypeClient == undefined || grantTypeClient == null) {
        throw "Missing the required parameter 'grantTypeClient' when calling getTokenByClient";
      }


      var pathParams = {
      };
      var queryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['access_token'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = GrantClient;

      return this.apiClient.callApi(
        '/oauth2/token?Client', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getTokenByMeeting operation.
     * @callback module:api/AuthenticationApi~getTokenByMeetingCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GrantMeeting} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Authentication via Meeting Grant Type
     * This is not a traditional OAuth grant type, but it behaves closely to the password grant type. This level of authentication allows for obtaining access to the meeting only. If a Moderator passcode is sent, moderator privileges are granted. If an Attendee access code is passed, the access token will have a limited scope of access that an attendee has within a meeting.
     * @param {module:model/GrantTypeMeeting} grantTypeMeeting Contains information about the type of grant you are requesting.
     * @param {module:api/AuthenticationApi~getTokenByMeetingCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GrantMeeting}
     */
    this.getTokenByMeeting = function(grantTypeMeeting, callback) {
      var postBody = grantTypeMeeting;

      // verify the required parameter 'grantTypeMeeting' is set
      if (grantTypeMeeting == undefined || grantTypeMeeting == null) {
        throw "Missing the required parameter 'grantTypeMeeting' when calling getTokenByMeeting";
      }


      var pathParams = {
      };
      var queryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['access_token'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = GrantMeeting;

      return this.apiClient.callApi(
        '/oauth2/token?Meeting', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }

    /**
     * Callback function to receive the result of the getTokenByPassword operation.
     * @callback module:api/AuthenticationApi~getTokenByPasswordCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GrantPassword} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Authentication via Password Grant Type
     * An access token can be obtained by using a user’s username and password.
     * @param {module:model/GrantTypePassword} grantTypePassword Contains information about the type of grant you are requesting.
     * @param {module:api/AuthenticationApi~getTokenByPasswordCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GrantPassword}
     */
    this.getTokenByPassword = function(grantTypePassword, callback) {
      var postBody = grantTypePassword;

      // verify the required parameter 'grantTypePassword' is set
      if (grantTypePassword == undefined || grantTypePassword == null) {
        throw "Missing the required parameter 'grantTypePassword' when calling getTokenByPassword";
      }


      var pathParams = {
      };
      var queryParams = {
      };
      var headerParams = {
      };
      var formParams = {
      };

      var authNames = ['access_token'];
      var contentTypes = ['application/json'];
      var accepts = ['application/json'];
      var returnType = GrantPassword;

      return this.apiClient.callApi(
        '/oauth2/token?Password', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, callback
      );
    }
  };

  return exports;
}));
