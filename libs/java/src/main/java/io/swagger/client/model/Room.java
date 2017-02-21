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


package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;


/**
 * Room
 */
@javax.annotation.Generated(value = "class io.swagger.codegen.languages.JavaClientCodegen", date = "2017-02-21T14:13:24.966-07:00")
public class Room   {
  @SerializedName("id")
  private Integer id = null;

  @SerializedName("numericId")
  private String numericId = null;

  @SerializedName("name")
  private String name = null;

  @SerializedName("originPopId")
  private Integer originPopId = null;

  @SerializedName("isLargeMeeting")
  private Boolean isLargeMeeting = null;

  @SerializedName("showVideoAnimations")
  private Boolean showVideoAnimations = null;

  @SerializedName("backgroundImage")
  private String backgroundImage = null;

  @SerializedName("isModeratorLess")
  private Boolean isModeratorLess = null;

  @SerializedName("welcomeMessage")
  private String welcomeMessage = null;

  @SerializedName("disallowChat")
  private Boolean disallowChat = null;

  @SerializedName("encryptionType")
  private String encryptionType = null;

  @SerializedName("showAllParticipantsInIcs")
  private Boolean showAllParticipantsInIcs = null;

  @SerializedName("participantPasscode")
  private String participantPasscode = null;

  @SerializedName("publishMeeting")
  private Boolean publishMeeting = null;

  @SerializedName("moderatorLess")
  private Boolean moderatorLess = null;

  @SerializedName("videoBestFit")
  private Boolean videoBestFit = null;

  @SerializedName("muteParticipantsOnEntry")
  private Boolean muteParticipantsOnEntry = null;

  @SerializedName("enforceMeetingEncryption")
  private Boolean enforceMeetingEncryption = null;

  @SerializedName("enforceMeetingEncryptionAllowPSTN")
  private Boolean enforceMeetingEncryptionAllowPSTN = null;

  @SerializedName("idleTimeout")
  private Integer idleTimeout = null;

  @SerializedName("defaultLayout")
  private String defaultLayout = null;

  @SerializedName("playAudioAlerts")
  private Boolean playAudioAlerts = null;

  @SerializedName("personalMeetingId")
  private Integer personalMeetingId = null;

  @SerializedName("moderatorPasscode")
  private String moderatorPasscode = null;

   /**
   * Unique identifier for room.
   * @return id
  **/
  @ApiModelProperty(example = "null", value = "Unique identifier for room.")
  public Integer getId() {
    return id;
  }

  public Room numericId(String numericId) {
    this.numericId = numericId;
    return this;
  }

   /**
   * Unique identifier for room.
   * @return numericId
  **/
  @ApiModelProperty(example = "null", value = "Unique identifier for room.")
  public String getNumericId() {
    return numericId;
  }

  public void setNumericId(String numericId) {
    this.numericId = numericId;
  }

  public Room name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Name of the room.
   * @return name
  **/
  @ApiModelProperty(example = "null", value = "Name of the room.")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public Room originPopId(Integer originPopId) {
    this.originPopId = originPopId;
    return this;
  }

   /**
   * Get originPopId
   * @return originPopId
  **/
  @ApiModelProperty(example = "null", value = "")
  public Integer getOriginPopId() {
    return originPopId;
  }

  public void setOriginPopId(Integer originPopId) {
    this.originPopId = originPopId;
  }

  public Room isLargeMeeting(Boolean isLargeMeeting) {
    this.isLargeMeeting = isLargeMeeting;
    return this;
  }

   /**
   * Get isLargeMeeting
   * @return isLargeMeeting
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getIsLargeMeeting() {
    return isLargeMeeting;
  }

  public void setIsLargeMeeting(Boolean isLargeMeeting) {
    this.isLargeMeeting = isLargeMeeting;
  }

  public Room showVideoAnimations(Boolean showVideoAnimations) {
    this.showVideoAnimations = showVideoAnimations;
    return this;
  }

   /**
   * Get showVideoAnimations
   * @return showVideoAnimations
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getShowVideoAnimations() {
    return showVideoAnimations;
  }

  public void setShowVideoAnimations(Boolean showVideoAnimations) {
    this.showVideoAnimations = showVideoAnimations;
  }

  public Room backgroundImage(String backgroundImage) {
    this.backgroundImage = backgroundImage;
    return this;
  }

   /**
   * Get backgroundImage
   * @return backgroundImage
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getBackgroundImage() {
    return backgroundImage;
  }

  public void setBackgroundImage(String backgroundImage) {
    this.backgroundImage = backgroundImage;
  }

  public Room isModeratorLess(Boolean isModeratorLess) {
    this.isModeratorLess = isModeratorLess;
    return this;
  }

   /**
   * Get isModeratorLess
   * @return isModeratorLess
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getIsModeratorLess() {
    return isModeratorLess;
  }

  public void setIsModeratorLess(Boolean isModeratorLess) {
    this.isModeratorLess = isModeratorLess;
  }

  public Room welcomeMessage(String welcomeMessage) {
    this.welcomeMessage = welcomeMessage;
    return this;
  }

   /**
   * Get welcomeMessage
   * @return welcomeMessage
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getWelcomeMessage() {
    return welcomeMessage;
  }

  public void setWelcomeMessage(String welcomeMessage) {
    this.welcomeMessage = welcomeMessage;
  }

  public Room disallowChat(Boolean disallowChat) {
    this.disallowChat = disallowChat;
    return this;
  }

   /**
   * Get disallowChat
   * @return disallowChat
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getDisallowChat() {
    return disallowChat;
  }

  public void setDisallowChat(Boolean disallowChat) {
    this.disallowChat = disallowChat;
  }

  public Room encryptionType(String encryptionType) {
    this.encryptionType = encryptionType;
    return this;
  }

   /**
   * Get encryptionType
   * @return encryptionType
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getEncryptionType() {
    return encryptionType;
  }

  public void setEncryptionType(String encryptionType) {
    this.encryptionType = encryptionType;
  }

  public Room showAllParticipantsInIcs(Boolean showAllParticipantsInIcs) {
    this.showAllParticipantsInIcs = showAllParticipantsInIcs;
    return this;
  }

   /**
   * Get showAllParticipantsInIcs
   * @return showAllParticipantsInIcs
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getShowAllParticipantsInIcs() {
    return showAllParticipantsInIcs;
  }

  public void setShowAllParticipantsInIcs(Boolean showAllParticipantsInIcs) {
    this.showAllParticipantsInIcs = showAllParticipantsInIcs;
  }

  public Room participantPasscode(String participantPasscode) {
    this.participantPasscode = participantPasscode;
    return this;
  }

   /**
   * Get participantPasscode
   * @return participantPasscode
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getParticipantPasscode() {
    return participantPasscode;
  }

  public void setParticipantPasscode(String participantPasscode) {
    this.participantPasscode = participantPasscode;
  }

  public Room publishMeeting(Boolean publishMeeting) {
    this.publishMeeting = publishMeeting;
    return this;
  }

   /**
   * Get publishMeeting
   * @return publishMeeting
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getPublishMeeting() {
    return publishMeeting;
  }

  public void setPublishMeeting(Boolean publishMeeting) {
    this.publishMeeting = publishMeeting;
  }

  public Room moderatorLess(Boolean moderatorLess) {
    this.moderatorLess = moderatorLess;
    return this;
  }

   /**
   * Get moderatorLess
   * @return moderatorLess
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getModeratorLess() {
    return moderatorLess;
  }

  public void setModeratorLess(Boolean moderatorLess) {
    this.moderatorLess = moderatorLess;
  }

  public Room videoBestFit(Boolean videoBestFit) {
    this.videoBestFit = videoBestFit;
    return this;
  }

   /**
   * Get videoBestFit
   * @return videoBestFit
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getVideoBestFit() {
    return videoBestFit;
  }

  public void setVideoBestFit(Boolean videoBestFit) {
    this.videoBestFit = videoBestFit;
  }

  public Room muteParticipantsOnEntry(Boolean muteParticipantsOnEntry) {
    this.muteParticipantsOnEntry = muteParticipantsOnEntry;
    return this;
  }

   /**
   * Get muteParticipantsOnEntry
   * @return muteParticipantsOnEntry
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getMuteParticipantsOnEntry() {
    return muteParticipantsOnEntry;
  }

  public void setMuteParticipantsOnEntry(Boolean muteParticipantsOnEntry) {
    this.muteParticipantsOnEntry = muteParticipantsOnEntry;
  }

  public Room enforceMeetingEncryption(Boolean enforceMeetingEncryption) {
    this.enforceMeetingEncryption = enforceMeetingEncryption;
    return this;
  }

   /**
   * Get enforceMeetingEncryption
   * @return enforceMeetingEncryption
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getEnforceMeetingEncryption() {
    return enforceMeetingEncryption;
  }

  public void setEnforceMeetingEncryption(Boolean enforceMeetingEncryption) {
    this.enforceMeetingEncryption = enforceMeetingEncryption;
  }

  public Room enforceMeetingEncryptionAllowPSTN(Boolean enforceMeetingEncryptionAllowPSTN) {
    this.enforceMeetingEncryptionAllowPSTN = enforceMeetingEncryptionAllowPSTN;
    return this;
  }

   /**
   * Get enforceMeetingEncryptionAllowPSTN
   * @return enforceMeetingEncryptionAllowPSTN
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getEnforceMeetingEncryptionAllowPSTN() {
    return enforceMeetingEncryptionAllowPSTN;
  }

  public void setEnforceMeetingEncryptionAllowPSTN(Boolean enforceMeetingEncryptionAllowPSTN) {
    this.enforceMeetingEncryptionAllowPSTN = enforceMeetingEncryptionAllowPSTN;
  }

  public Room idleTimeout(Integer idleTimeout) {
    this.idleTimeout = idleTimeout;
    return this;
  }

   /**
   * Get idleTimeout
   * @return idleTimeout
  **/
  @ApiModelProperty(example = "null", value = "")
  public Integer getIdleTimeout() {
    return idleTimeout;
  }

  public void setIdleTimeout(Integer idleTimeout) {
    this.idleTimeout = idleTimeout;
  }

  public Room defaultLayout(String defaultLayout) {
    this.defaultLayout = defaultLayout;
    return this;
  }

   /**
   * Get defaultLayout
   * @return defaultLayout
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getDefaultLayout() {
    return defaultLayout;
  }

  public void setDefaultLayout(String defaultLayout) {
    this.defaultLayout = defaultLayout;
  }

  public Room playAudioAlerts(Boolean playAudioAlerts) {
    this.playAudioAlerts = playAudioAlerts;
    return this;
  }

   /**
   * Get playAudioAlerts
   * @return playAudioAlerts
  **/
  @ApiModelProperty(example = "null", value = "")
  public Boolean getPlayAudioAlerts() {
    return playAudioAlerts;
  }

  public void setPlayAudioAlerts(Boolean playAudioAlerts) {
    this.playAudioAlerts = playAudioAlerts;
  }

  public Room personalMeetingId(Integer personalMeetingId) {
    this.personalMeetingId = personalMeetingId;
    return this;
  }

   /**
   * Get personalMeetingId
   * @return personalMeetingId
  **/
  @ApiModelProperty(example = "null", value = "")
  public Integer getPersonalMeetingId() {
    return personalMeetingId;
  }

  public void setPersonalMeetingId(Integer personalMeetingId) {
    this.personalMeetingId = personalMeetingId;
  }

  public Room moderatorPasscode(String moderatorPasscode) {
    this.moderatorPasscode = moderatorPasscode;
    return this;
  }

   /**
   * Get moderatorPasscode
   * @return moderatorPasscode
  **/
  @ApiModelProperty(example = "null", value = "")
  public String getModeratorPasscode() {
    return moderatorPasscode;
  }

  public void setModeratorPasscode(String moderatorPasscode) {
    this.moderatorPasscode = moderatorPasscode;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Room room = (Room) o;
    return Objects.equals(this.id, room.id) &&
        Objects.equals(this.numericId, room.numericId) &&
        Objects.equals(this.name, room.name) &&
        Objects.equals(this.originPopId, room.originPopId) &&
        Objects.equals(this.isLargeMeeting, room.isLargeMeeting) &&
        Objects.equals(this.showVideoAnimations, room.showVideoAnimations) &&
        Objects.equals(this.backgroundImage, room.backgroundImage) &&
        Objects.equals(this.isModeratorLess, room.isModeratorLess) &&
        Objects.equals(this.welcomeMessage, room.welcomeMessage) &&
        Objects.equals(this.disallowChat, room.disallowChat) &&
        Objects.equals(this.encryptionType, room.encryptionType) &&
        Objects.equals(this.showAllParticipantsInIcs, room.showAllParticipantsInIcs) &&
        Objects.equals(this.participantPasscode, room.participantPasscode) &&
        Objects.equals(this.publishMeeting, room.publishMeeting) &&
        Objects.equals(this.moderatorLess, room.moderatorLess) &&
        Objects.equals(this.videoBestFit, room.videoBestFit) &&
        Objects.equals(this.muteParticipantsOnEntry, room.muteParticipantsOnEntry) &&
        Objects.equals(this.enforceMeetingEncryption, room.enforceMeetingEncryption) &&
        Objects.equals(this.enforceMeetingEncryptionAllowPSTN, room.enforceMeetingEncryptionAllowPSTN) &&
        Objects.equals(this.idleTimeout, room.idleTimeout) &&
        Objects.equals(this.defaultLayout, room.defaultLayout) &&
        Objects.equals(this.playAudioAlerts, room.playAudioAlerts) &&
        Objects.equals(this.personalMeetingId, room.personalMeetingId) &&
        Objects.equals(this.moderatorPasscode, room.moderatorPasscode);
  }

  @Override
  public int hashCode() {
    return Objects.hash(id, numericId, name, originPopId, isLargeMeeting, showVideoAnimations, backgroundImage, isModeratorLess, welcomeMessage, disallowChat, encryptionType, showAllParticipantsInIcs, participantPasscode, publishMeeting, moderatorLess, videoBestFit, muteParticipantsOnEntry, enforceMeetingEncryption, enforceMeetingEncryptionAllowPSTN, idleTimeout, defaultLayout, playAudioAlerts, personalMeetingId, moderatorPasscode);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Room {\n");
    
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    numericId: ").append(toIndentedString(numericId)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    originPopId: ").append(toIndentedString(originPopId)).append("\n");
    sb.append("    isLargeMeeting: ").append(toIndentedString(isLargeMeeting)).append("\n");
    sb.append("    showVideoAnimations: ").append(toIndentedString(showVideoAnimations)).append("\n");
    sb.append("    backgroundImage: ").append(toIndentedString(backgroundImage)).append("\n");
    sb.append("    isModeratorLess: ").append(toIndentedString(isModeratorLess)).append("\n");
    sb.append("    welcomeMessage: ").append(toIndentedString(welcomeMessage)).append("\n");
    sb.append("    disallowChat: ").append(toIndentedString(disallowChat)).append("\n");
    sb.append("    encryptionType: ").append(toIndentedString(encryptionType)).append("\n");
    sb.append("    showAllParticipantsInIcs: ").append(toIndentedString(showAllParticipantsInIcs)).append("\n");
    sb.append("    participantPasscode: ").append(toIndentedString(participantPasscode)).append("\n");
    sb.append("    publishMeeting: ").append(toIndentedString(publishMeeting)).append("\n");
    sb.append("    moderatorLess: ").append(toIndentedString(moderatorLess)).append("\n");
    sb.append("    videoBestFit: ").append(toIndentedString(videoBestFit)).append("\n");
    sb.append("    muteParticipantsOnEntry: ").append(toIndentedString(muteParticipantsOnEntry)).append("\n");
    sb.append("    enforceMeetingEncryption: ").append(toIndentedString(enforceMeetingEncryption)).append("\n");
    sb.append("    enforceMeetingEncryptionAllowPSTN: ").append(toIndentedString(enforceMeetingEncryptionAllowPSTN)).append("\n");
    sb.append("    idleTimeout: ").append(toIndentedString(idleTimeout)).append("\n");
    sb.append("    defaultLayout: ").append(toIndentedString(defaultLayout)).append("\n");
    sb.append("    playAudioAlerts: ").append(toIndentedString(playAudioAlerts)).append("\n");
    sb.append("    personalMeetingId: ").append(toIndentedString(personalMeetingId)).append("\n");
    sb.append("    moderatorPasscode: ").append(toIndentedString(moderatorPasscode)).append("\n");
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

