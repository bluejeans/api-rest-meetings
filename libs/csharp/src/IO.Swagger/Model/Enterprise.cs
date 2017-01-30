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
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace IO.Swagger.Model
{
    /// <summary>
    /// Enterprise
    /// </summary>
    [DataContract]
    public partial class Enterprise :  IEquatable<Enterprise>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Enterprise" /> class.
        /// </summary>
        /// <param name="EnterpriseAdmin">Is this user an administrator for this enterprise?.</param>
        /// <param name="JoinDate">Date of enterprise join.</param>
        /// <param name="ExpiryDate">Date of expiration; null if not set.</param>
        public Enterprise(bool? EnterpriseAdmin = null, int? JoinDate = null, int? ExpiryDate = null)
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
    }

}
