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
    /// AnalyticsFeedbackScores
    /// </summary>
    [DataContract]
    public partial class AnalyticsFeedbackScores :  IEquatable<AnalyticsFeedbackScores>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="AnalyticsFeedbackScores" /> class.
        /// </summary>
        /// <param name="Great">Great.</param>
        /// <param name="Okay">Okay.</param>
        /// <param name="Bad">Bad.</param>
        /// <param name="Poor">Poor.</param>
        /// <param name="Good">Good.</param>
        public AnalyticsFeedbackScores(int? Great = default(int?), int? Okay = default(int?), int? Bad = default(int?), int? Poor = default(int?), int? Good = default(int?))
        {
            this.Great = Great;
            this.Okay = Okay;
            this.Bad = Bad;
            this.Poor = Poor;
            this.Good = Good;
        }
        
        /// <summary>
        /// Gets or Sets Great
        /// </summary>
        [DataMember(Name="Great", EmitDefaultValue=false)]
        public int? Great { get; set; }
        /// <summary>
        /// Gets or Sets Okay
        /// </summary>
        [DataMember(Name="Okay", EmitDefaultValue=false)]
        public int? Okay { get; set; }
        /// <summary>
        /// Gets or Sets Bad
        /// </summary>
        [DataMember(Name="Bad", EmitDefaultValue=false)]
        public int? Bad { get; set; }
        /// <summary>
        /// Gets or Sets Poor
        /// </summary>
        [DataMember(Name="Poor", EmitDefaultValue=false)]
        public int? Poor { get; set; }
        /// <summary>
        /// Gets or Sets Good
        /// </summary>
        [DataMember(Name="Good", EmitDefaultValue=false)]
        public int? Good { get; set; }
        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class AnalyticsFeedbackScores {\n");
            sb.Append("  Great: ").Append(Great).Append("\n");
            sb.Append("  Okay: ").Append(Okay).Append("\n");
            sb.Append("  Bad: ").Append(Bad).Append("\n");
            sb.Append("  Poor: ").Append(Poor).Append("\n");
            sb.Append("  Good: ").Append(Good).Append("\n");
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
            return this.Equals(obj as AnalyticsFeedbackScores);
        }

        /// <summary>
        /// Returns true if AnalyticsFeedbackScores instances are equal
        /// </summary>
        /// <param name="other">Instance of AnalyticsFeedbackScores to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(AnalyticsFeedbackScores other)
        {
            // credit: http://stackoverflow.com/a/10454552/677735
            if (other == null)
                return false;

            return 
                (
                    this.Great == other.Great ||
                    this.Great != null &&
                    this.Great.Equals(other.Great)
                ) && 
                (
                    this.Okay == other.Okay ||
                    this.Okay != null &&
                    this.Okay.Equals(other.Okay)
                ) && 
                (
                    this.Bad == other.Bad ||
                    this.Bad != null &&
                    this.Bad.Equals(other.Bad)
                ) && 
                (
                    this.Poor == other.Poor ||
                    this.Poor != null &&
                    this.Poor.Equals(other.Poor)
                ) && 
                (
                    this.Good == other.Good ||
                    this.Good != null &&
                    this.Good.Equals(other.Good)
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
                if (this.Great != null)
                    hash = hash * 59 + this.Great.GetHashCode();
                if (this.Okay != null)
                    hash = hash * 59 + this.Okay.GetHashCode();
                if (this.Bad != null)
                    hash = hash * 59 + this.Bad.GetHashCode();
                if (this.Poor != null)
                    hash = hash * 59 + this.Poor.GetHashCode();
                if (this.Good != null)
                    hash = hash * 59 + this.Good.GetHashCode();
                return hash;
            }
        }

        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        { 
            yield break;
        }
    }

}
