/**
 * BlueJeans onVideo REST API
 * _Video That Works Where You Do._  This site provides developers access to API's from BlueJean's onVideo meeting service.  From here you will be able to make actual API calls to manage User Accounts, Meetings, and Recordings.  Also, you can pull analytical data as well retrieve current state information.  With these API's  you should be able to quickly integrate **BlueJeans** video into your applications.     # Authentication All API transactions (excluding Authentication) require an access token per **OAuth standards**.  BlueJeans provides multiple methods for obtaining an access token.  Additionally there are diffferent scopes of token access. ## Grant Types Bluejeans provides 3 different methods for users to Authenticate.  Successful authentication allows BlueJeans to grant an access token to the user. * Authorization Code Grant – Authenticate via a BlueJeans page, and receive an authorization code. Submit authorization with other tokens and receive an access code. (\"three-legged OAuth\") * Password Credentials Grant – Authenticate with a Username and password and receives an access code. (\"two-legged OAuth\"); * Client Credentials Grant – Similar to Password Grant (\"two-legged OAuth\"). ## Access & Permissions BlueJeans defines 3 levels of API access into the system.  When an access token is granted, it carries one of these 3 levels.  The scope of system functionality depends upon the token's access level. * Meeting-level – scope of APIs is limited to individual meetings. * User-level – scope depends on the requested permissions. * App-level – provisioned either by BlueJeans personnel, or the BlueJeans Enterprise Admin, an app, is issued a client key and secret key. These tokens then are used by the BlueJeans Authentication API to receive the token. The token's scope provides access to the entire enterprise and all of its users.  All endpoints in this document that require **Enterprise Admin** access will be marked as such. # Getting Started Before you start using the API's on this site, you must first have a BlueJeans account.  With your BlueJean credentials, use one of the Authentication methods to obtain an access token. - Click on the Authorize button at the top of page - Enter your access token in the field marked \"api_key\" Now the web site will automatically include your access token on all API calls you make. 
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
    instance = new BlueJeansOnVideoRestApi.GrantCodeScope();
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

  describe('GrantCodeScope', function() {
    it('should create an instance of GrantCodeScope', function() {
      // uncomment below and update the code to test GrantCodeScope
      //var instane = new BlueJeansOnVideoRestApi.GrantCodeScope();
      //expect(instance).to.be.a(BlueJeansOnVideoRestApi.GrantCodeScope);
    });

    it('should have the property user (base name: "user")', function() {
      // uncomment below and update the code to test the property user
      //var instane = new BlueJeansOnVideoRestApi.GrantCodeScope();
      //expect(instance).to.be();
    });

    it('should have the property appPermissions (base name: "appPermissions")', function() {
      // uncomment below and update the code to test the property appPermissions
      //var instane = new BlueJeansOnVideoRestApi.GrantCodeScope();
      //expect(instance).to.be();
    });

    it('should have the property partitionName (base name: "partitionName")', function() {
      // uncomment below and update the code to test the property partitionName
      //var instane = new BlueJeansOnVideoRestApi.GrantCodeScope();
      //expect(instance).to.be();
    });

    it('should have the property partition (base name: "partition")', function() {
      // uncomment below and update the code to test the property partition
      //var instane = new BlueJeansOnVideoRestApi.GrantCodeScope();
      //expect(instance).to.be();
    });

    it('should have the property bearerPermissions (base name: "bearerPermissions")', function() {
      // uncomment below and update the code to test the property bearerPermissions
      //var instane = new BlueJeansOnVideoRestApi.GrantCodeScope();
      //expect(instance).to.be();
    });

    it('should have the property clientId (base name: "clientId")', function() {
      // uncomment below and update the code to test the property clientId
      //var instane = new BlueJeansOnVideoRestApi.GrantCodeScope();
      //expect(instance).to.be();
    });

  });

}));
