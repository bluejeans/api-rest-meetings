/**
 * BlueJeans onVideo REST API
 *  # Video That Works Where You Do. This site provides developers access to API's from BlueJean's onVideo meeting service.  From here you will be able to make actual API calls to manage User Accounts, Meetings, and Recordings.  Also, you can pull analytical data and current state information.  With these API's  you should be able to quickly integrate **BlueJeans** video administration into your applications.     ## Getting Started Before you start using BlueJeans' API's, you must first have a BlueJeans account enabled for API Access.  Contact [BlueJeans Support](mailto:Support@BlueJeans.com) for assistance.  <br /><br />Once you have an account, you may start writing application code to authenticate and make API calls.  *Alternatively*, you can use this developer site to test the BlueJeans' API's and develop a level of familiarity before you write production code.  <br /> ### To Make API Calls from This Site If you want to use this developer site to try various BlueJeans' API's, here are the steps required to authenticate and enable your Developer Session to place API calls. 1. Choose Method for Authenticating       * Click on the desired Authentication method from below.      * Click on the **Try It Out** button. 1. Make Authentication request      * Follow API's instructions and input the API parameters.      * Click on the blue **Execute** button.      * If successful, the API returns with JSON data containing a field called **access_token**.  Copy/save this value. 1. Authorize BlueJeans Developer Session.      * Click on the green **Authorize button**.       * The site will show you a pop-up window for authorization.      * Enter your access token in the field named **api_key**      * Click on the **Authorize** button  Your current BlueJeans developer session is now authenticated and ready to place API calls.  The web site will automatically include your access token on any API calls you make.  ## About onVideo Authentication All API transactions (excluding Authentication) require an access token per **OAuth standards**.  BlueJeans provides multiple methods for obtaining an access token.  Additionally there are diffferent scopes of token access. ### Grant Types Bluejeans provides 4 different methods for users to Authenticate.  Successful authentication allows BlueJeans to grant an access token to perform API operations. * Password Credentials Grant – Authenticate with a username and password and receive an access token with user level permission. Known as two-legged OAuth. * Meeting Credentials Grant – Authenticate with a meeting ID and meeting passcode and receive an access token with meeting level permission. Known as two-legged OAuth. * Client Credentials Grant –  Authenticate with a client ID and client secret and receive an access token with enterprise level permission. Known as two-legged OAuth. * Authorization Code Grant – Authentication for your developer's application occurs through a redirection to a BlueJeans authentication page. The application receives an authorization code to be submitted, along with other tokens, to receive an access token. Known as three-legged OAuth. For more information please refer to the [OAuth specification](https://oauth.net/). ### Access & Permissions BlueJeans defines 3 levels of API access into the system.  When an access token is granted, it carries one of these 3 levels.  The scope of system functionality depends upon the token's access level. * Meeting-level – Scope of APIs is limited to individual meetings. * User-level – Scope depends on the requested permissions. * App-level – provisioned either by BlueJeans personnel, or the BlueJeans Enterprise Admin, an app, is issued a client key and secret key. These tokens then are used by the BlueJeans Authentication API to receive the token. The token's scope provides access to the entire enterprise and all of its users. All endpoints in this document that require **Enterprise Admin** access will be marked as such. 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: brandon@bluejeans.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'));
  } else {
    // Browser globals (root is window)
    if (!root.BlueJeansOnVideoRestApi) {
      root.BlueJeansOnVideoRestApi = {};
    }
    root.BlueJeansOnVideoRestApi.Room = factory(root.BlueJeansOnVideoRestApi.ApiClient);
  }
}(this, function(ApiClient) {
  'use strict';




  /**
   * The Room model module.
   * @module model/Room
   * @version 1.0.0
   */

  /**
   * Constructs a new <code>Room</code>.
   * @alias module:model/Room
   * @class
   */
  var exports = function() {
    var _this = this;

























  };

  /**
   * Constructs a <code>Room</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Room} obj Optional instance to populate.
   * @return {module:model/Room} The populated <code>Room</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();

      if (data.hasOwnProperty('id')) {
        obj['id'] = ApiClient.convertToType(data['id'], 'Number');
      }
      if (data.hasOwnProperty('numericId')) {
        obj['numericId'] = ApiClient.convertToType(data['numericId'], 'String');
      }
      if (data.hasOwnProperty('name')) {
        obj['name'] = ApiClient.convertToType(data['name'], 'String');
      }
      if (data.hasOwnProperty('originPopId')) {
        obj['originPopId'] = ApiClient.convertToType(data['originPopId'], 'Number');
      }
      if (data.hasOwnProperty('isLargeMeeting')) {
        obj['isLargeMeeting'] = ApiClient.convertToType(data['isLargeMeeting'], 'Boolean');
      }
      if (data.hasOwnProperty('showVideoAnimations')) {
        obj['showVideoAnimations'] = ApiClient.convertToType(data['showVideoAnimations'], 'Boolean');
      }
      if (data.hasOwnProperty('backgroundImage')) {
        obj['backgroundImage'] = ApiClient.convertToType(data['backgroundImage'], 'String');
      }
      if (data.hasOwnProperty('isModeratorLess')) {
        obj['isModeratorLess'] = ApiClient.convertToType(data['isModeratorLess'], 'Boolean');
      }
      if (data.hasOwnProperty('welcomeMessage')) {
        obj['welcomeMessage'] = ApiClient.convertToType(data['welcomeMessage'], 'String');
      }
      if (data.hasOwnProperty('disallowChat')) {
        obj['disallowChat'] = ApiClient.convertToType(data['disallowChat'], 'Boolean');
      }
      if (data.hasOwnProperty('encryptionType')) {
        obj['encryptionType'] = ApiClient.convertToType(data['encryptionType'], 'String');
      }
      if (data.hasOwnProperty('showAllParticipantsInIcs')) {
        obj['showAllParticipantsInIcs'] = ApiClient.convertToType(data['showAllParticipantsInIcs'], 'Boolean');
      }
      if (data.hasOwnProperty('participantPasscode')) {
        obj['participantPasscode'] = ApiClient.convertToType(data['participantPasscode'], 'String');
      }
      if (data.hasOwnProperty('publishMeeting')) {
        obj['publishMeeting'] = ApiClient.convertToType(data['publishMeeting'], 'Boolean');
      }
      if (data.hasOwnProperty('moderatorLess')) {
        obj['moderatorLess'] = ApiClient.convertToType(data['moderatorLess'], 'Boolean');
      }
      if (data.hasOwnProperty('videoBestFit')) {
        obj['videoBestFit'] = ApiClient.convertToType(data['videoBestFit'], 'Boolean');
      }
      if (data.hasOwnProperty('muteParticipantsOnEntry')) {
        obj['muteParticipantsOnEntry'] = ApiClient.convertToType(data['muteParticipantsOnEntry'], 'Boolean');
      }
      if (data.hasOwnProperty('enforceMeetingEncryption')) {
        obj['enforceMeetingEncryption'] = ApiClient.convertToType(data['enforceMeetingEncryption'], 'Boolean');
      }
      if (data.hasOwnProperty('enforceMeetingEncryptionAllowPSTN')) {
        obj['enforceMeetingEncryptionAllowPSTN'] = ApiClient.convertToType(data['enforceMeetingEncryptionAllowPSTN'], 'Boolean');
      }
      if (data.hasOwnProperty('idleTimeout')) {
        obj['idleTimeout'] = ApiClient.convertToType(data['idleTimeout'], 'Number');
      }
      if (data.hasOwnProperty('defaultLayout')) {
        obj['defaultLayout'] = ApiClient.convertToType(data['defaultLayout'], 'String');
      }
      if (data.hasOwnProperty('playAudioAlerts')) {
        obj['playAudioAlerts'] = ApiClient.convertToType(data['playAudioAlerts'], 'Boolean');
      }
      if (data.hasOwnProperty('personalMeetingId')) {
        obj['personalMeetingId'] = ApiClient.convertToType(data['personalMeetingId'], 'Number');
      }
      if (data.hasOwnProperty('moderatorPasscode')) {
        obj['moderatorPasscode'] = ApiClient.convertToType(data['moderatorPasscode'], 'String');
      }
    }
    return obj;
  }

  /**
   * Unique identifier for room.
   * @member {Number} id
   */
  exports.prototype['id'] = undefined;
  /**
   * Unique identifier for room.
   * @member {String} numericId
   */
  exports.prototype['numericId'] = undefined;
  /**
   * Name of the room.
   * @member {String} name
   */
  exports.prototype['name'] = undefined;
  /**
   * @member {Number} originPopId
   */
  exports.prototype['originPopId'] = undefined;
  /**
   * @member {Boolean} isLargeMeeting
   */
  exports.prototype['isLargeMeeting'] = undefined;
  /**
   * @member {Boolean} showVideoAnimations
   */
  exports.prototype['showVideoAnimations'] = undefined;
  /**
   * @member {String} backgroundImage
   */
  exports.prototype['backgroundImage'] = undefined;
  /**
   * @member {Boolean} isModeratorLess
   */
  exports.prototype['isModeratorLess'] = undefined;
  /**
   * @member {String} welcomeMessage
   */
  exports.prototype['welcomeMessage'] = undefined;
  /**
   * @member {Boolean} disallowChat
   */
  exports.prototype['disallowChat'] = undefined;
  /**
   * @member {String} encryptionType
   */
  exports.prototype['encryptionType'] = undefined;
  /**
   * @member {Boolean} showAllParticipantsInIcs
   */
  exports.prototype['showAllParticipantsInIcs'] = undefined;
  /**
   * @member {String} participantPasscode
   */
  exports.prototype['participantPasscode'] = undefined;
  /**
   * @member {Boolean} publishMeeting
   */
  exports.prototype['publishMeeting'] = undefined;
  /**
   * @member {Boolean} moderatorLess
   */
  exports.prototype['moderatorLess'] = undefined;
  /**
   * @member {Boolean} videoBestFit
   */
  exports.prototype['videoBestFit'] = undefined;
  /**
   * @member {Boolean} muteParticipantsOnEntry
   */
  exports.prototype['muteParticipantsOnEntry'] = undefined;
  /**
   * @member {Boolean} enforceMeetingEncryption
   */
  exports.prototype['enforceMeetingEncryption'] = undefined;
  /**
   * @member {Boolean} enforceMeetingEncryptionAllowPSTN
   */
  exports.prototype['enforceMeetingEncryptionAllowPSTN'] = undefined;
  /**
   * @member {Number} idleTimeout
   */
  exports.prototype['idleTimeout'] = undefined;
  /**
   * @member {String} defaultLayout
   */
  exports.prototype['defaultLayout'] = undefined;
  /**
   * @member {Boolean} playAudioAlerts
   */
  exports.prototype['playAudioAlerts'] = undefined;
  /**
   * @member {Number} personalMeetingId
   */
  exports.prototype['personalMeetingId'] = undefined;
  /**
   * @member {String} moderatorPasscode
   */
  exports.prototype['moderatorPasscode'] = undefined;



  return exports;
}));

