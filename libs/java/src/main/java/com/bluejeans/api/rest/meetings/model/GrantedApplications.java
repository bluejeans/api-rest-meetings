/*
 * BlueJeans Meetings REST API
 *  ## Video That Works Where You Do. <p>This site provides developers access to APIs from BlueJean's Meetings meeting service.  From here you can see and try actual API calls to manage User Accounts, Meetings, and Recordings, pull Analytical Data and Current State information.</p>    <nosdk> <hr> <div> <div class=\"key\">     <a href=\"./basics.html\" target=\"_\"><img class=\"keyimg\" src=\"./img/bjnmeeting.png\"/></a> </div> <div class=\"keybox\"> Basic instructions about What is a BlueJeans Meeting, and Getting Started Using API's, are <a href=\"./basics.html\" target=\"_blank\">available here <i class=\"glyphicon glyphicon-new-window\"></i></a>. </div> </div> <hr> <alert>2/21/2019</alert> Change response of Change layout and Endpoint API's to 204<br/> 12/03/2018 Add API for setting user profile photograph.<br/> 10/17/2018 Updated API field definitions for time variables to be 64-bit .<br/> 7/23/2018 Corrected errors in API definition file.<br/> 7/10/2018 Deprecated some Command Center API's.  Exposed API's that Summarize usage.<br/> 7/06/2018 Added API for changing ownership of recordings.<br/> 6/28/2018 Restored Create Enterprise Account, added Enterprise and User Profile Tag API's.<br/> 6/01/2018 Clarified Access Token requirements for meeting endpoint API's.<br/> 5/21/2018 Corrected return model for meeting history call.<br/> </nosdk> <hr> 
 *
 * OpenAPI spec version: 1.0.4402212019
 * Contact: glenn@bluejeans.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package com.bluejeans.api.rest.meetings.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * GrantedApplications
 */

public class GrantedApplications {
  @SerializedName("appName")
  private String appName = null;

  @SerializedName("appDescription")
  private String appDescription = null;

  @SerializedName("clientId")
  private String clientId = null;

  @SerializedName("userId")
  private Integer userId = null;

  @SerializedName("scope")
  private String scope = null;

  public GrantedApplications appName(String appName) {
    this.appName = appName;
    return this;
  }

   /**
   * Name of the Application
   * @return appName
  **/
  @ApiModelProperty(value = "Name of the Application")
  public String getAppName() {
    return appName;
  }

  public void setAppName(String appName) {
    this.appName = appName;
  }

  public GrantedApplications appDescription(String appDescription) {
    this.appDescription = appDescription;
    return this;
  }

   /**
   * A summary of the client application.
   * @return appDescription
  **/
  @ApiModelProperty(value = "A summary of the client application.")
  public String getAppDescription() {
    return appDescription;
  }

  public void setAppDescription(String appDescription) {
    this.appDescription = appDescription;
  }

  public GrantedApplications clientId(String clientId) {
    this.clientId = clientId;
    return this;
  }

   /**
   * The client ID will be generated on creation of the application. Normally, a 32 character hexadecimal numeric string.
   * @return clientId
  **/
  @ApiModelProperty(value = "The client ID will be generated on creation of the application. Normally, a 32 character hexadecimal numeric string.")
  public String getClientId() {
    return clientId;
  }

  public void setClientId(String clientId) {
    this.clientId = clientId;
  }

  public GrantedApplications userId(Integer userId) {
    this.userId = userId;
    return this;
  }

   /**
   * Same user ID as passed in path parameter.
   * @return userId
  **/
  @ApiModelProperty(value = "Same user ID as passed in path parameter.")
  public Integer getUserId() {
    return userId;
  }

  public void setUserId(Integer userId) {
    this.userId = userId;
  }

  public GrantedApplications scope(String scope) {
    this.scope = scope;
    return this;
  }

   /**
   * Comma-delimited list of granted permissions to the application.
   * @return scope
  **/
  @ApiModelProperty(value = "Comma-delimited list of granted permissions to the application.")
  public String getScope() {
    return scope;
  }

  public void setScope(String scope) {
    this.scope = scope;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GrantedApplications grantedApplications = (GrantedApplications) o;
    return Objects.equals(this.appName, grantedApplications.appName) &&
        Objects.equals(this.appDescription, grantedApplications.appDescription) &&
        Objects.equals(this.clientId, grantedApplications.clientId) &&
        Objects.equals(this.userId, grantedApplications.userId) &&
        Objects.equals(this.scope, grantedApplications.scope);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appName, appDescription, clientId, userId, scope);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GrantedApplications {\n");
    
    sb.append("    appName: ").append(toIndentedString(appName)).append("\n");
    sb.append("    appDescription: ").append(toIndentedString(appDescription)).append("\n");
    sb.append("    clientId: ").append(toIndentedString(clientId)).append("\n");
    sb.append("    userId: ").append(toIndentedString(userId)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
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

