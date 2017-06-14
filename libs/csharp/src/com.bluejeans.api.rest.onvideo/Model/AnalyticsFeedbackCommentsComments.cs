/* 
 * BlueJeans onVideo REST API
 *
 *  # Video That Works Where You Do. This site provides developers access to API's from BlueJean's onVideo meeting service.  From here you will be able to make actual API calls to manage User Accounts, Meetings, and Recordings.  Also, you can pull analytical data and current state information.  With these API's  you should be able to quickly integrate **BlueJeans** video administration into your applications.     ## Getting Started Before you start using BlueJeans' API's, you must first have a BlueJeans account enabled for API Access.  Contact [BlueJeans Support](mailto:Support@BlueJeans.com) for assistance.  <br /><br />Once you have an account, you may start writing application code to authenticate and make API calls.  *Alternatively*, you can use this developer site to test the BlueJeans' API's and develop a level of familiarity before you write production code.  <br /> ### To Make API Calls from This Site If you want to use this developer site to try various BlueJeans' API's, here are the steps required to authenticate and enable your Developer Session to place API calls. 1. Choose Method for Authenticating       * Click on the desired Authentication method from below.      * Click on the **Try It Out** button. 1. Make Authentication request      * Follow API's instructions and input the API parameters.      * Click on the blue **Execute** button.      * If successful, the API returns with JSON data containing a field called **access_token**.  Copy/save this value. 1. Authorize BlueJeans Developer Session.      * Click on the green **Authorize button**.       * The site will show you a pop-up window for authorization.      * Enter your access token in the field named **api_key**      * Click on the **Authorize** button  Your current BlueJeans developer session is now authenticated and ready to place API calls.  The web site will automatically include your access token on any API calls you make.  ## About onVideo Authentication All API transactions (excluding Authentication) require an access token per **OAuth standards**.  BlueJeans provides multiple methods for obtaining an access token.  Additionally there are diffferent scopes of token access. ### Grant Types Bluejeans provides 4 different methods for users to Authenticate.  Successful authentication allows BlueJeans to grant an access token to perform API operations. * Password Credentials Grant – Authenticate with a username and password and receive an access token with user level permission. Known as two-legged OAuth. * Meeting Credentials Grant – Authenticate with a meeting ID and meeting passcode and receive an access token with meeting level permission. Known as two-legged OAuth. * Client Credentials Grant –  Authenticate with a client ID and client secret and receive an access token with enterprise level permission. Known as two-legged OAuth. * Authorization Code Grant – Authentication for your developer's application occurs through a redirection to a BlueJeans authentication page. The application receives an authorization code to be submitted, along with other tokens, to receive an access token. Known as three-legged OAuth. For more information please refer to the [OAuth specification](https://oauth.net/). ### Access & Permissions BlueJeans defines 3 levels of API access into the system.  When an access token is granted, it carries one of these 3 levels.  The scope of system functionality depends upon the token's access level. * Meeting-level – Scope of APIs is limited to individual meetings. * User-level – Scope depends on the requested permissions. * App-level – provisioned either by BlueJeans personnel, or the BlueJeans Enterprise Admin, an app, is issued a client key and secret key. These tokens then are used by the BlueJeans Authentication API to receive the token. The token's scope provides access to the entire enterprise and all of its users. All endpoints in this document that require **Enterprise Admin** access will be marked as such. 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: brandon@bluejeans.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;

namespace com.bluejeans.api.rest.onvideo.Model
{
    /// <summary>
    /// AnalyticsFeedbackCommentsComments
    /// </summary>
    [DataContract]
    public partial class AnalyticsFeedbackCommentsComments :  IEquatable<AnalyticsFeedbackCommentsComments>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="AnalyticsFeedbackCommentsComments" /> class.
        /// </summary>
        /// <param name="QualarooFeedback">The comment rating left by the user..</param>
        /// <param name="MeetingUuid">The UUID of the meeting..</param>
        /// <param name="Callguid">Callguid.</param>
        /// <param name="QualarooComments">The comment left by the user..</param>
        public AnalyticsFeedbackCommentsComments(string QualarooFeedback = default(string), string MeetingUuid = default(string), string Callguid = default(string), string QualarooComments = default(string))
        {
            this.QualarooFeedback = QualarooFeedback;
            this.MeetingUuid = MeetingUuid;
            this.Callguid = Callguid;
            this.QualarooComments = QualarooComments;
        }
        
        /// <summary>
        /// The comment rating left by the user.
        /// </summary>
        /// <value>The comment rating left by the user.</value>
        [DataMember(Name="qualaroo_feedback", EmitDefaultValue=false)]
        public string QualarooFeedback { get; set; }
        /// <summary>
        /// The UUID of the meeting.
        /// </summary>
        /// <value>The UUID of the meeting.</value>
        [DataMember(Name="meeting_uuid", EmitDefaultValue=false)]
        public string MeetingUuid { get; set; }
        /// <summary>
        /// Gets or Sets Callguid
        /// </summary>
        [DataMember(Name="callguid", EmitDefaultValue=false)]
        public string Callguid { get; set; }
        /// <summary>
        /// The comment left by the user.
        /// </summary>
        /// <value>The comment left by the user.</value>
        [DataMember(Name="qualaroo_comments", EmitDefaultValue=false)]
        public string QualarooComments { get; set; }
        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class AnalyticsFeedbackCommentsComments {\n");
            sb.Append("  QualarooFeedback: ").Append(QualarooFeedback).Append("\n");
            sb.Append("  MeetingUuid: ").Append(MeetingUuid).Append("\n");
            sb.Append("  Callguid: ").Append(Callguid).Append("\n");
            sb.Append("  QualarooComments: ").Append(QualarooComments).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            // credit: http://stackoverflow.com/a/10454552/677735
            return this.Equals(obj as AnalyticsFeedbackCommentsComments);
        }

        /// <summary>
        /// Returns true if AnalyticsFeedbackCommentsComments instances are equal
        /// </summary>
        /// <param name="other">Instance of AnalyticsFeedbackCommentsComments to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(AnalyticsFeedbackCommentsComments other)
        {
            // credit: http://stackoverflow.com/a/10454552/677735
            if (other == null)
                return false;

            return 
                (
                    this.QualarooFeedback == other.QualarooFeedback ||
                    this.QualarooFeedback != null &&
                    this.QualarooFeedback.Equals(other.QualarooFeedback)
                ) && 
                (
                    this.MeetingUuid == other.MeetingUuid ||
                    this.MeetingUuid != null &&
                    this.MeetingUuid.Equals(other.MeetingUuid)
                ) && 
                (
                    this.Callguid == other.Callguid ||
                    this.Callguid != null &&
                    this.Callguid.Equals(other.Callguid)
                ) && 
                (
                    this.QualarooComments == other.QualarooComments ||
                    this.QualarooComments != null &&
                    this.QualarooComments.Equals(other.QualarooComments)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            // credit: http://stackoverflow.com/a/263416/677735
            unchecked // Overflow is fine, just wrap
            {
                int hash = 41;
                // Suitable nullity checks etc, of course :)
                if (this.QualarooFeedback != null)
                    hash = hash * 59 + this.QualarooFeedback.GetHashCode();
                if (this.MeetingUuid != null)
                    hash = hash * 59 + this.MeetingUuid.GetHashCode();
                if (this.Callguid != null)
                    hash = hash * 59 + this.Callguid.GetHashCode();
                if (this.QualarooComments != null)
                    hash = hash * 59 + this.QualarooComments.GetHashCode();
                return hash;
            }
        }

        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        { 
            yield break;
        }
    }

}
