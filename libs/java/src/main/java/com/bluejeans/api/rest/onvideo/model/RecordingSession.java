/*
 * BlueJeans onVideo REST API
 *  # Video That Works Where You Do. This site provides developers access to API's from BlueJean's onVideo meeting service.  From here you will be able to make actual API calls to manage User Accounts, Meetings, and Recordings.  Also, you can pull analytical data and current state information.  With these API's  you should be able to quickly integrate **BlueJeans** video administration into your applications.     ## Getting Started Before you start using BlueJeans' API's, you must first have a BlueJeans account enabled for API Access.  Contact [BlueJeans Support](mailto:Support@BlueJeans.com) for assistance.  <br /><br />Once you have an account, you may start writing application code to authenticate and make API calls.  *Alternatively*, you can use this developer site to test the BlueJeans' API's and develop a level of familiarity before you write production code.  <br /> ### To Make API Calls from This Site If you want to use this developer site to try various BlueJeans' API's, here are the steps required to authenticate and enable your Developer Session to place API calls. 1. Choose Method for Authenticating       * Click on the desired Authentication method from below.      * Click on the **Try It Out** button. 1. Make Authentication request      * Follow API's instructions and input the API parameters.      * Click on the blue **Execute** button.      * If successful, the API returns with JSON data containing a field called **access_token**.  Copy/save this value. 1. Authorize BlueJeans Developer Session.      * Click on the green **Authorize button**.       * The site will show you a pop-up window for authorization.      * Enter your access token in the field named **api_key**      * Click on the **Authorize** button  Your current BlueJeans developer session is now authenticated and ready to place API calls.  The web site will automatically include your access token on any API calls you make.  ## About onVideo Authentication All API transactions (excluding Authentication) require an access token per **OAuth standards**.  BlueJeans provides multiple methods for obtaining an access token.  Additionally there are diffferent scopes of token access. ### Grant Types Bluejeans provides 4 different methods for users to Authenticate.  Successful authentication allows BlueJeans to grant an access token to perform API operations. * Password Credentials Grant – Authenticate with a username and password and receive an access token with user level permission. Known as two-legged OAuth. * Meeting Credentials Grant – Authenticate with a meeting ID and meeting passcode and receive an access token with meeting level permission. Known as two-legged OAuth. * Client Credentials Grant –  Authenticate with a client ID and client secret and receive an access token with enterprise level permission. Known as two-legged OAuth. * Authorization Code Grant – Authentication for your developer's application occurs through a redirection to a BlueJeans authentication page. The application receives an authorization code to be submitted, along with other tokens, to receive an access token. Known as three-legged OAuth. For more information please refer to the [OAuth specification](https://oauth.net/). ### Access & Permissions BlueJeans defines 3 levels of API access into the system.  When an access token is granted, it carries one of these 3 levels.  The scope of system functionality depends upon the token's access level. * Meeting-level – Scope of APIs is limited to individual meetings. * User-level – Scope depends on the requested permissions. * App-level – provisioned either by BlueJeans personnel, or the BlueJeans Enterprise Admin, an app, is issued a client key and secret key. These tokens then are used by the BlueJeans Authentication API to receive the token. The token's scope provides access to the entire enterprise and all of its users. All endpoints in this document that require **Enterprise Admin** access will be marked as such. 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: brandon@bluejeans.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.bluejeans.api.rest.onvideo.model;

import java.util.Objects;
import com.bluejeans.api.rest.onvideo.model.RecordingSessionStartedBy;
import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

/**
 * RecordingSession
 */

public class RecordingSession {
  @SerializedName("id")
  private Integer id = null;

  @SerializedName("contentStatus")
  private String contentStatus = null;

  @SerializedName("recordingType")
  private String recordingType = null;

  @SerializedName("contentId")
  private Integer contentId = null;

  @SerializedName("thumbnailUrl")
  private String thumbnailUrl = null;

  @SerializedName("startTimeOffset")
  private Integer startTimeOffset = null;

  @SerializedName("endTimeOffset")
  private Integer endTimeOffset = null;

  @SerializedName("duration")
  private Integer duration = null;

  @SerializedName("startedBy")
  private RecordingSessionStartedBy startedBy = null;

  @SerializedName("stoppedBy")
  private RecordingSessionStartedBy stoppedBy = null;

  public RecordingSession id(Integer id) {
    this.id = id;
    return this;
  }

   /**
   * Get id
   * @return id
  **/
  @ApiModelProperty(example = "null", value = "")
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }

  public RecordingSession contentStatus(String contentStatus) {
    this.contentStatus = contentStatus;
    return this;
  }

   /**
   * Get contentStatus
   * @return contentStatus
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getContentStatus() {
    return contentStatus;
  }

  public void setContentStatus(String contentStatus) {
    this.contentStatus = contentStatus;
  }

  public RecordingSession recordingType(String recordingType) {
    this.recordingType = recordingType;
    return this;
  }

   /**
   * Get recordingType
   * @return recordingType
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getRecordingType() {
    return recordingType;
  }

  public void setRecordingType(String recordingType) {
    this.recordingType = recordingType;
  }

  public RecordingSession contentId(Integer contentId) {
    this.contentId = contentId;
    return this;
  }

   /**
   * Get contentId
   * @return contentId
  **/
  @ApiModelProperty(example = "null", value = "")
  public Integer getContentId() {
    return contentId;
  }

  public void setContentId(Integer contentId) {
    this.contentId = contentId;
  }

  public RecordingSession thumbnailUrl(String thumbnailUrl) {
    this.thumbnailUrl = thumbnailUrl;
    return this;
  }

   /**
   * Get thumbnailUrl
   * @return thumbnailUrl
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getThumbnailUrl() {
    return thumbnailUrl;
  }

  public void setThumbnailUrl(String thumbnailUrl) {
    this.thumbnailUrl = thumbnailUrl;
  }

  public RecordingSession startTimeOffset(Integer startTimeOffset) {
    this.startTimeOffset = startTimeOffset;
    return this;
  }

   /**
   * Get startTimeOffset
   * @return startTimeOffset
  **/
  @ApiModelProperty(example = "null", value = "")
  public Integer getStartTimeOffset() {
    return startTimeOffset;
  }

  public void setStartTimeOffset(Integer startTimeOffset) {
    this.startTimeOffset = startTimeOffset;
  }

  public RecordingSession endTimeOffset(Integer endTimeOffset) {
    this.endTimeOffset = endTimeOffset;
    return this;
  }

   /**
   * Get endTimeOffset
   * @return endTimeOffset
  **/
  @ApiModelProperty(example = "null", value = "")
  public Integer getEndTimeOffset() {
    return endTimeOffset;
  }

  public void setEndTimeOffset(Integer endTimeOffset) {
    this.endTimeOffset = endTimeOffset;
  }

  public RecordingSession duration(Integer duration) {
    this.duration = duration;
    return this;
  }

   /**
   * Get duration
   * @return duration
  **/
  @ApiModelProperty(example = "null", value = "")
  public Integer getDuration() {
    return duration;
  }

  public void setDuration(Integer duration) {
    this.duration = duration;
  }

  public RecordingSession startedBy(RecordingSessionStartedBy startedBy) {
    this.startedBy = startedBy;
    return this;
  }

   /**
   * Get startedBy
   * @return startedBy
  **/
  @ApiModelProperty(example = "null", value = "")
  public RecordingSessionStartedBy getStartedBy() {
    return startedBy;
  }

  public void setStartedBy(RecordingSessionStartedBy startedBy) {
    this.startedBy = startedBy;
  }

  public RecordingSession stoppedBy(RecordingSessionStartedBy stoppedBy) {
    this.stoppedBy = stoppedBy;
    return this;
  }

   /**
   * Get stoppedBy
   * @return stoppedBy
  **/
  @ApiModelProperty(example = "null", value = "")
  public RecordingSessionStartedBy getStoppedBy() {
    return stoppedBy;
  }

  public void setStoppedBy(RecordingSessionStartedBy stoppedBy) {
    this.stoppedBy = stoppedBy;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RecordingSession recordingSession = (RecordingSession) o;
    return Objects.equals(this.id, recordingSession.id) &&
        Objects.equals(this.contentStatus, recordingSession.contentStatus) &&
        Objects.equals(this.recordingType, recordingSession.recordingType) &&
        Objects.equals(this.contentId, recordingSession.contentId) &&
        Objects.equals(this.thumbnailUrl, recordingSession.thumbnailUrl) &&
        Objects.equals(this.startTimeOffset, recordingSession.startTimeOffset) &&
        Objects.equals(this.endTimeOffset, recordingSession.endTimeOffset) &&
        Objects.equals(this.duration, recordingSession.duration) &&
        Objects.equals(this.startedBy, recordingSession.startedBy) &&
        Objects.equals(this.stoppedBy, recordingSession.stoppedBy);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, contentStatus, recordingType, contentId, thumbnailUrl, startTimeOffset, endTimeOffset, duration, startedBy, stoppedBy);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RecordingSession {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    contentStatus: ").append(toIndentedString(contentStatus)).append("\n");
    sb.append("    recordingType: ").append(toIndentedString(recordingType)).append("\n");
    sb.append("    contentId: ").append(toIndentedString(contentId)).append("\n");
    sb.append("    thumbnailUrl: ").append(toIndentedString(thumbnailUrl)).append("\n");
    sb.append("    startTimeOffset: ").append(toIndentedString(startTimeOffset)).append("\n");
    sb.append("    endTimeOffset: ").append(toIndentedString(endTimeOffset)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    startedBy: ").append(toIndentedString(startedBy)).append("\n");
    sb.append("    stoppedBy: ").append(toIndentedString(stoppedBy)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }
  
}

