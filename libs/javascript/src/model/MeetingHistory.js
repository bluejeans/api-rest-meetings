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
    define(['ApiClient', 'model/MeetingHistoryLeaderInfo', 'model/MeetingHistoryParticipantList'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./MeetingHistoryLeaderInfo'), require('./MeetingHistoryParticipantList'));
  } else {
    // Browser globals (root is window)
    if (!root.BlueJeansOnVideoRestApi) {
      root.BlueJeansOnVideoRestApi = {};
    }
    root.BlueJeansOnVideoRestApi.MeetingHistory = factory(root.BlueJeansOnVideoRestApi.ApiClient, root.BlueJeansOnVideoRestApi.MeetingHistoryLeaderInfo, root.BlueJeansOnVideoRestApi.MeetingHistoryParticipantList);
  }
}(this, function(ApiClient, MeetingHistoryLeaderInfo, MeetingHistoryParticipantList) {
  'use strict';




  /**
   * The MeetingHistory model module.
   * @module model/MeetingHistory
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>MeetingHistory</code>.
   * @alias module:model/MeetingHistory
   * @class
   */
  var exports = function() {
    var _this = this;


























  };

  /**
   * Constructs a <code>MeetingHistory</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/MeetingHistory} obj Optional instance to populate.
   * @return {module:model/MeetingHistory} The populated <code>MeetingHistory</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('meetingGuid')) {
        obj['meetingGuid'] = ApiClient.convertToType(data['meetingGuid'], 'String');
      }
      if (data.hasOwnProperty('meetingNumericId')) {
        obj['meetingNumericId'] = ApiClient.convertToType(data['meetingNumericId'], 'String');
      }
      if (data.hasOwnProperty('title')) {
        obj['title'] = ApiClient.convertToType(data['title'], 'String');
      }
      if (data.hasOwnProperty('description')) {
        obj['description'] = ApiClient.convertToType(data['description'], 'String');
      }
      if (data.hasOwnProperty('leaderInfo')) {
        obj['leaderInfo'] = MeetingHistoryLeaderInfo.constructFromObject(data['leaderInfo']);
      }
      if (data.hasOwnProperty('userId')) {
        obj['userId'] = ApiClient.convertToType(data['userId'], 'Integer');
      }
      if (data.hasOwnProperty('meetingDuration')) {
        obj['meetingDuration'] = ApiClient.convertToType(data['meetingDuration'], 'Integer');
      }
      if (data.hasOwnProperty('maxParticipantCount')) {
        obj['maxParticipantCount'] = ApiClient.convertToType(data['maxParticipantCount'], 'Integer');
      }
      if (data.hasOwnProperty('totalParticipantMinutes')) {
        obj['totalParticipantMinutes'] = ApiClient.convertToType(data['totalParticipantMinutes'], 'Integer');
      }
      if (data.hasOwnProperty('maxParticipantMinutes')) {
        obj['maxParticipantMinutes'] = ApiClient.convertToType(data['maxParticipantMinutes'], 'Integer');
      }
      if (data.hasOwnProperty('extraParticipantMinutes')) {
        obj['extraParticipantMinutes'] = ApiClient.convertToType(data['extraParticipantMinutes'], 'Integer');
      }
      if (data.hasOwnProperty('isdnEndpoints')) {
        obj['isdnEndpoints'] = ApiClient.convertToType(data['isdnEndpoints'], 'Integer');
      }
      if (data.hasOwnProperty('totalDialoutMinutes')) {
        obj['totalDialoutMinutes'] = ApiClient.convertToType(data['totalDialoutMinutes'], 'Integer');
      }
      if (data.hasOwnProperty('totalTollFreeMinutes')) {
        obj['totalTollFreeMinutes'] = ApiClient.convertToType(data['totalTollFreeMinutes'], 'Integer');
      }
      if (data.hasOwnProperty('callDIDMinutes')) {
        obj['callDIDMinutes'] = ApiClient.convertToType(data['callDIDMinutes'], 'Integer');
      }
      if (data.hasOwnProperty('startTime')) {
        obj['startTime'] = ApiClient.convertToType(data['startTime'], 'Integer');
      }
      if (data.hasOwnProperty('endTime')) {
        obj['endTime'] = ApiClient.convertToType(data['endTime'], 'Integer');
      }
      if (data.hasOwnProperty('meetingStatus')) {
        obj['meetingStatus'] = ApiClient.convertToType(data['meetingStatus'], 'String');
      }
      if (data.hasOwnProperty('meetingThumbnail')) {
        obj['meetingThumbnail'] = ApiClient.convertToType(data['meetingThumbnail'], 'String');
      }
      if (data.hasOwnProperty('startTimeZone')) {
        obj['startTimeZone'] = ApiClient.convertToType(data['startTimeZone'], 'String');
      }
      if (data.hasOwnProperty('processingStatus')) {
        obj['processingStatus'] = ApiClient.convertToType(data['processingStatus'], 'String');
      }
      if (data.hasOwnProperty('concurrentCalls')) {
        obj['concurrentCalls'] = ApiClient.convertToType(data['concurrentCalls'], 'String');
      }
      if (data.hasOwnProperty('uploadStatus')) {
        obj['uploadStatus'] = ApiClient.convertToType(data['uploadStatus'], 'String');
      }
      if (data.hasOwnProperty('pstnonly')) {
        obj['pstnonly'] = ApiClient.convertToType(data['pstnonly'], 'Boolean');
      }
      if (data.hasOwnProperty('participantList')) {
        obj['participantList'] = ApiClient.convertToType(data['participantList'], [MeetingHistoryParticipantList]);
      }
    }
    return obj;
  }

  /**
   * @member {String} meetingGuid
   */
  exports.prototype['meetingGuid'] = undefined;
  /**
   * @member {String} meetingNumericId
   */
  exports.prototype['meetingNumericId'] = undefined;
  /**
   * @member {String} title
   */
  exports.prototype['title'] = undefined;
  /**
   * @member {String} description
   */
  exports.prototype['description'] = undefined;
  /**
   * @member {module:model/MeetingHistoryLeaderInfo} leaderInfo
   */
  exports.prototype['leaderInfo'] = undefined;
  /**
   * @member {Integer} userId
   */
  exports.prototype['userId'] = undefined;
  /**
   * @member {Integer} meetingDuration
   */
  exports.prototype['meetingDuration'] = undefined;
  /**
   * @member {Integer} maxParticipantCount
   */
  exports.prototype['maxParticipantCount'] = undefined;
  /**
   * @member {Integer} totalParticipantMinutes
   */
  exports.prototype['totalParticipantMinutes'] = undefined;
  /**
   * @member {Integer} maxParticipantMinutes
   */
  exports.prototype['maxParticipantMinutes'] = undefined;
  /**
   * @member {Integer} extraParticipantMinutes
   */
  exports.prototype['extraParticipantMinutes'] = undefined;
  /**
   * @member {Integer} isdnEndpoints
   */
  exports.prototype['isdnEndpoints'] = undefined;
  /**
   * @member {Integer} totalDialoutMinutes
   */
  exports.prototype['totalDialoutMinutes'] = undefined;
  /**
   * @member {Integer} totalTollFreeMinutes
   */
  exports.prototype['totalTollFreeMinutes'] = undefined;
  /**
   * @member {Integer} callDIDMinutes
   */
  exports.prototype['callDIDMinutes'] = undefined;
  /**
   * @member {Integer} startTime
   */
  exports.prototype['startTime'] = undefined;
  /**
   * @member {Integer} endTime
   */
  exports.prototype['endTime'] = undefined;
  /**
   * @member {module:model/MeetingHistory.MeetingStatusEnum} meetingStatus
   */
  exports.prototype['meetingStatus'] = undefined;
  /**
   * @member {String} meetingThumbnail
   */
  exports.prototype['meetingThumbnail'] = undefined;
  /**
   * @member {String} startTimeZone
   */
  exports.prototype['startTimeZone'] = undefined;
  /**
   * @member {module:model/MeetingHistory.ProcessingStatusEnum} processingStatus
   */
  exports.prototype['processingStatus'] = undefined;
  /**
   * @member {String} concurrentCalls
   */
  exports.prototype['concurrentCalls'] = undefined;
  /**
   * @member {String} uploadStatus
   */
  exports.prototype['uploadStatus'] = undefined;
  /**
   * @member {Boolean} pstnonly
   */
  exports.prototype['pstnonly'] = undefined;
  /**
   * @member {Array.<module:model/MeetingHistoryParticipantList>} participantList
   */
  exports.prototype['participantList'] = undefined;


  /**
   * Allowed values for the <code>meetingStatus</code> property.
   * @enum {String}
   * @readonly
   */
  exports.MeetingStatusEnum = {
    /**
     * value: "Complete"
     * @const
     */
    "Complete": "Complete"  };

  /**
   * Allowed values for the <code>processingStatus</code> property.
   * @enum {String}
   * @readonly
   */
  exports.ProcessingStatusEnum = {
    /**
     * value: "PROCESSED"
     * @const
     */
    "PROCESSED": "PROCESSED"  };


  return exports;
}));


