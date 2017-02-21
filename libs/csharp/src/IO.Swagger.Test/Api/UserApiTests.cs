/* 
 * BlueJeans onVideo REST API
 *
 * _Video That Works Where You Do, from the world's leader in cloud video communication._ # Authentication Each API request that is sent to BlueJeans requires an access token, which is obtained through the BlueJeans Authentication API. There are several methods (grant types) for obtaining an access token, which follow the OAuth2.0 specification. ## Grant Types * Authorization Code Grant – This grant type is used in an authentication flow commonly referred to as \"three-legged OAuth\". The user authenticates via a BlueJeans page, which provides an authorization code. This code, along with a few other elements, can be used to obtain an access code. * Password Credentials Grant – This grant type is used in a two-legged OAuth flow. Username and password are sent to retrieve an access code. * Client Credentials Grant – This grant type is used in a two-legged OAuth flow.  ## Access & Permissions The access level that is associated with each access token is referred to as the scope. There are three basic levels of access that BlueJeans allows, which affect the level of scope.  Three access levels exist within the Blue Jeans service today. * Meeting-level – Authentication takes place using a meeting ID and passcode, and the scope is limited to APIs that relate to the individual meeting. * User-level – Authentication either takes place via three-legged OAuth, or else a direct authorization token request containing a username or password. Access level depends on the requested scope permissions. * App-level – An application is provisioned either by BlueJeans personnel, or within the BlueJeans Enterprise Admin interface. When provisioning an app, a client key and secret are provided, which is then used to obtain an access token, via the BlueJeans Authentication API. The scope that is associated with the token will provide access to an entire enterprise and all of its users.  All endpoints in this document that require Enterprise Admin access will be marked as such. ## Testing In order to make effective use of this page, you will first use one of the authentication methods to obtain an access token. Once the token is given, use the Authenticate button up in the header to store the token. Each BlueJeans API called after that will use the access token provided. 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: brandon@bluejeans.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using IO.Swagger.Client;
using IO.Swagger.Api;
using IO.Swagger.Model;

namespace IO.Swagger.Test
{
    /// <summary>
    ///  Class for testing UserApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class UserApiTests
    {
        private UserApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new UserApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of UserApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' UserApi
            //Assert.IsInstanceOfType(typeof(UserApi), instance, "instance is a UserApi");
        }

        
        /// <summary>
        /// Test GetDefaultMeeting
        /// </summary>
        [Test]
        public void GetDefaultMeetingTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //int? userId = null;
            //var response = instance.GetDefaultMeeting(userId);
            //Assert.IsInstanceOf<List<Meeting>> (response, "response is List<Meeting>");
        }
        
        /// <summary>
        /// Test GetEnterpriseProfile
        /// </summary>
        [Test]
        public void GetEnterpriseProfileTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //int? userId = null;
            //var response = instance.GetEnterpriseProfile(userId);
            //Assert.IsInstanceOf<Enterprise> (response, "response is Enterprise");
        }
        
        /// <summary>
        /// Test GetRoom
        /// </summary>
        [Test]
        public void GetRoomTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //int? userId = null;
            //var response = instance.GetRoom(userId);
            //Assert.IsInstanceOf<Room> (response, "response is Room");
        }
        
        /// <summary>
        /// Test GetUser
        /// </summary>
        [Test]
        public void GetUserTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //int? userId = null;
            //var response = instance.GetUser(userId);
            //Assert.IsInstanceOf<User> (response, "response is User");
        }
        
        /// <summary>
        /// Test UpdateRoom
        /// </summary>
        [Test]
        public void UpdateRoomTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //int? userId = null;
            //Room room = null;
            //var response = instance.UpdateRoom(userId, room);
            //Assert.IsInstanceOf<Room> (response, "response is Room");
        }
        
        /// <summary>
        /// Test UpdateUser
        /// </summary>
        [Test]
        public void UpdateUserTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //int? userId = null;
            //User user = null;
            //var response = instance.UpdateUser(userId, user);
            //Assert.IsInstanceOf<User> (response, "response is User");
        }
        
    }

}
