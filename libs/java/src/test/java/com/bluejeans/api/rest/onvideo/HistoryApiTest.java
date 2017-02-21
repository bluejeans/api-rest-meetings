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


package com.bluejeans.api.rest.onvideo;

import com.bluejeans.api.rest.ApiException;
import io.swagger.client.model.Error;
import io.swagger.client.model.Recording;
import io.swagger.client.model.MeetingHistory;
import io.swagger.client.model.RecordingSummary;
import io.swagger.client.model.Meeting;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for HistoryApi
 */
public class HistoryApiTest {

    private final HistoryApi api = new HistoryApi();

    
    /**
     * Get Recording
     *
     * This endpoint retrieves the details about a meeting recording.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void getRecordingTest() throws ApiException {
        Integer userId = null;
        Integer recordingEntityId = null;
        // Recording response = api.getRecording(userId, recordingEntityId);

        // TODO: test validations
    }
    
    /**
     * List Meetings
     *
     * This endpoint retrieves a list of meetings.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listMeetingsByEnterpriseTest() throws ApiException {
        Integer enterpriseId = null;
        // List<MeetingHistory> response = api.listMeetingsByEnterprise(enterpriseId);

        // TODO: test validations
    }
    
    /**
     * List Meetings
     *
     * This endpoint retrieves a list of meetings.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listMeetingsByUserTest() throws ApiException {
        Integer userId = null;
        String meetingId = null;
        String startDate = null;
        String endDate = null;
        Integer pageSize = null;
        Integer pageNumber = null;
        String order = null;
        // List<MeetingHistory> response = api.listMeetingsByUser(userId, meetingId, startDate, endDate, pageSize, pageNumber, order);

        // TODO: test validations
    }
    
    /**
     * List Meeting Recordings
     *
     * This endpoint retrieves a list of meeting recordings.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void listRecordingsTest() throws ApiException {
        Integer userId = null;
        Integer pageSize = null;
        Integer pageNumber = null;
        String sortBy = null;
        String order = null;
        // List<RecordingSummary> response = api.listRecordings(userId, pageSize, pageNumber, sortBy, order);

        // TODO: test validations
    }
    
    /**
     * List Meetings
     *
     * This endpoint retrieves a list of meetings.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void v1EnterpriseEnterpriseIdMeetingHistoryMeetingGuidGetTest() throws ApiException {
        Integer enterpriseId = null;
        String meetingGuid = null;
        // Meeting response = api.v1EnterpriseEnterpriseIdMeetingHistoryMeetingGuidGet(enterpriseId, meetingGuid);

        // TODO: test validations
    }
    
    /**
     * List Meetings
     *
     * This endpoint retrieves a list of meetings.
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void v1UserUserIdMeetingHistoryMeetingGuidGetTest() throws ApiException {
        Integer userId = null;
        String meetingGuid = null;
        // Meeting response = api.v1UserUserIdMeetingHistoryMeetingGuidGet(userId, meetingGuid);

        // TODO: test validations
    }
    
}
