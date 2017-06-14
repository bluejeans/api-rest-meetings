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
    /// Enterprise
    /// </summary>
    [DataContract]
    public partial class Enterprise :  IEquatable<Enterprise>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Enterprise" /> class.
        /// </summary>
        /// <param name="EnterpriseAdmin">Is this user an administrator for this enterprise?.</param>
        /// <param name="JoinDate">Date of enterprise join.</param>
        /// <param name="ExpiryDate">Date of expiration; null if not set.</param>
        public Enterprise(bool? EnterpriseAdmin = default(bool?), int? JoinDate = default(int?), int? ExpiryDate = default(int?))
        {
            this.EnterpriseAdmin = EnterpriseAdmin;
            this.JoinDate = JoinDate;
            this.ExpiryDate = ExpiryDate;
        }
        
        /// <summary>
        /// Unique identifier for the user.
        /// </summary>
        /// <value>Unique identifier for the user.</value>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public int? Id { get; private set; }
        /// <summary>
        /// Unique identifier for the enterprise.
        /// </summary>
        /// <value>Unique identifier for the enterprise.</value>
        [DataMember(Name="enterprise", EmitDefaultValue=false)]
        public int? _Enterprise { get; private set; }
        /// <summary>
        /// Is this user an administrator for this enterprise?
        /// </summary>
        /// <value>Is this user an administrator for this enterprise?</value>
        [DataMember(Name="enterpriseAdmin", EmitDefaultValue=false)]
        public bool? EnterpriseAdmin { get; set; }
        /// <summary>
        /// Date of enterprise join
        /// </summary>
        /// <value>Date of enterprise join</value>
        [DataMember(Name="joinDate", EmitDefaultValue=false)]
        public int? JoinDate { get; set; }
        /// <summary>
        /// Date of expiration; null if not set
        /// </summary>
        /// <value>Date of expiration; null if not set</value>
        [DataMember(Name="expiryDate", EmitDefaultValue=false)]
        public int? ExpiryDate { get; set; }
        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Enterprise {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  _Enterprise: ").Append(_Enterprise).Append("\n");
            sb.Append("  EnterpriseAdmin: ").Append(EnterpriseAdmin).Append("\n");
            sb.Append("  JoinDate: ").Append(JoinDate).Append("\n");
            sb.Append("  ExpiryDate: ").Append(ExpiryDate).Append("\n");
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
            return this.Equals(obj as Enterprise);
        }

        /// <summary>
        /// Returns true if Enterprise instances are equal
        /// </summary>
        /// <param name="other">Instance of Enterprise to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Enterprise other)
        {
            // credit: http://stackoverflow.com/a/10454552/677735
            if (other == null)
                return false;

            return 
                (
                    this.Id == other.Id ||
                    this.Id != null &&
                    this.Id.Equals(other.Id)
                ) && 
                (
                    this._Enterprise == other._Enterprise ||
                    this._Enterprise != null &&
                    this._Enterprise.Equals(other._Enterprise)
                ) && 
                (
                    this.EnterpriseAdmin == other.EnterpriseAdmin ||
                    this.EnterpriseAdmin != null &&
                    this.EnterpriseAdmin.Equals(other.EnterpriseAdmin)
                ) && 
                (
                    this.JoinDate == other.JoinDate ||
                    this.JoinDate != null &&
                    this.JoinDate.Equals(other.JoinDate)
                ) && 
                (
                    this.ExpiryDate == other.ExpiryDate ||
                    this.ExpiryDate != null &&
                    this.ExpiryDate.Equals(other.ExpiryDate)
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
                if (this.Id != null)
                    hash = hash * 59 + this.Id.GetHashCode();
                if (this._Enterprise != null)
                    hash = hash * 59 + this._Enterprise.GetHashCode();
                if (this.EnterpriseAdmin != null)
                    hash = hash * 59 + this.EnterpriseAdmin.GetHashCode();
                if (this.JoinDate != null)
                    hash = hash * 59 + this.JoinDate.GetHashCode();
                if (this.ExpiryDate != null)
                    hash = hash * 59 + this.ExpiryDate.GetHashCode();
                return hash;
            }
        }

        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        { 
            yield break;
        }
    }

}
