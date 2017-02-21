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
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.BlueJeansOnVideoRestApi);
  }
}(this, function(expect, BlueJeansOnVideoRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BlueJeansOnVideoRestApi.MeetingApi();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('MeetingApi', function() {
    describe('cancelMeeting', function() {
      it('should call cancelMeeting successfully', function(done) {
        //uncomment below and update the code to test cancelMeeting
        //instance.cancelMeeting(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createMeeting', function() {
      it('should call createMeeting successfully', function(done) {
        //uncomment below and update the code to test createMeeting
        //instance.createMeeting(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getDefaultMeeting', function() {
      it('should call getDefaultMeeting successfully', function(done) {
        //uncomment below and update the code to test getDefaultMeeting
        //instance.getDefaultMeeting(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getEndpointLayout', function() {
      it('should call getEndpointLayout successfully', function(done) {
        //uncomment below and update the code to test getEndpointLayout
        //instance.getEndpointLayout(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getMeeting', function() {
      it('should call getMeeting successfully', function(done) {
        //uncomment below and update the code to test getMeeting
        //instance.getMeeting(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateEndpointLayout', function() {
      it('should call updateEndpointLayout successfully', function(done) {
        //uncomment below and update the code to test updateEndpointLayout
        //instance.updateEndpointLayout(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateMeeting', function() {
      it('should call updateMeeting successfully', function(done) {
        //uncomment below and update the code to test updateMeeting
        //instance.updateMeeting(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdLiveMeetingsMeetingIdEndpointsEndpointGuidGet', function() {
      it('should call v1UserUserIdLiveMeetingsMeetingIdEndpointsEndpointGuidGet successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdLiveMeetingsMeetingIdEndpointsEndpointGuidGet
        //instance.v1UserUserIdLiveMeetingsMeetingIdEndpointsEndpointGuidGet(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdLiveMeetingsMeetingIdEndpointsEndpointGuidPut', function() {
      it('should call v1UserUserIdLiveMeetingsMeetingIdEndpointsEndpointGuidPut successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdLiveMeetingsMeetingIdEndpointsEndpointGuidPut
        //instance.v1UserUserIdLiveMeetingsMeetingIdEndpointsEndpointGuidPut(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdLiveMeetingsMeetingIdEndpointsGet', function() {
      it('should call v1UserUserIdLiveMeetingsMeetingIdEndpointsGet successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdLiveMeetingsMeetingIdEndpointsGet
        //instance.v1UserUserIdLiveMeetingsMeetingIdEndpointsGet(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdLiveMeetingsMeetingIdEndpointsPut', function() {
      it('should call v1UserUserIdLiveMeetingsMeetingIdEndpointsPut successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdLiveMeetingsMeetingIdEndpointsPut
        //instance.v1UserUserIdLiveMeetingsMeetingIdEndpointsPut(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdLiveMeetingsMeetingIdGet', function() {
      it('should call v1UserUserIdLiveMeetingsMeetingIdGet successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdLiveMeetingsMeetingIdGet
        //instance.v1UserUserIdLiveMeetingsMeetingIdGet(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdLiveMeetingsMeetingIdInvitePost', function() {
      it('should call v1UserUserIdLiveMeetingsMeetingIdInvitePost successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdLiveMeetingsMeetingIdInvitePost
        //instance.v1UserUserIdLiveMeetingsMeetingIdInvitePost(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdLiveMeetingsMeetingIdPairingCodeSIPPost', function() {
      it('should call v1UserUserIdLiveMeetingsMeetingIdPairingCodeSIPPost successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdLiveMeetingsMeetingIdPairingCodeSIPPost
        //instance.v1UserUserIdLiveMeetingsMeetingIdPairingCodeSIPPost(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdLiveMeetingsMeetingIdPut', function() {
      it('should call v1UserUserIdLiveMeetingsMeetingIdPut successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdLiveMeetingsMeetingIdPut
        //instance.v1UserUserIdLiveMeetingsMeetingIdPut(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdMeetingsMeetingIdNumbersGet', function() {
      it('should call v1UserUserIdMeetingsMeetingIdNumbersGet successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdMeetingsMeetingIdNumbersGet
        //instance.v1UserUserIdMeetingsMeetingIdNumbersGet(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1UserUserIdScheduledMeetingMeetingIdEmailsGet', function() {
      it('should call v1UserUserIdScheduledMeetingMeetingIdEmailsGet successfully', function(done) {
        //uncomment below and update the code to test v1UserUserIdScheduledMeetingMeetingIdEmailsGet
        //instance.v1UserUserIdScheduledMeetingMeetingIdEmailsGet(pet, function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
