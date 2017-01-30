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
    /// RecordingRecordingChapters
    /// </summary>
    [DataContract]
    public partial class RecordingRecordingChapters :  IEquatable<RecordingRecordingChapters>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="RecordingRecordingChapters" /> class.
        /// </summary>
        /// <param name="ChapterId">ChapterId.</param>
        /// <param name="Id">Id.</param>
        /// <param name="StartTimeOffset">StartTimeOffset.</param>
        /// <param name="EndTimeOffset">EndTimeOffset.</param>
        /// <param name="ChapterName">ChapterName.</param>
        /// <param name="TotalSize">TotalSize.</param>
        /// <param name="CompositeContentId">CompositeContentId.</param>
        /// <param name="CompositeContentStatus">CompositeContentStatus.</param>
        /// <param name="ParentRecordingId">ParentRecordingId.</param>
        /// <param name="ViewCount">ViewCount.</param>
        /// <param name="RecordingSessions">RecordingSessions.</param>
        public RecordingRecordingChapters(string ChapterId = null, int? Id = null, int? StartTimeOffset = null, int? EndTimeOffset = null, string ChapterName = null, int? TotalSize = null, int? CompositeContentId = null, string CompositeContentStatus = null, int? ParentRecordingId = null, int? ViewCount = null, List<RecordingRecordingSessions> RecordingSessions = null)
        {
            this.ChapterId = ChapterId;
            this.Id = Id;
            this.StartTimeOffset = StartTimeOffset;
            this.EndTimeOffset = EndTimeOffset;
            this.ChapterName = ChapterName;
            this.TotalSize = TotalSize;
            this.CompositeContentId = CompositeContentId;
            this.CompositeContentStatus = CompositeContentStatus;
            this.ParentRecordingId = ParentRecordingId;
            this.ViewCount = ViewCount;
            this.RecordingSessions = RecordingSessions;
        }
        
        /// <summary>
        /// Gets or Sets ChapterId
        /// </summary>
        [DataMember(Name="chapterId", EmitDefaultValue=false)]
        public string ChapterId { get; set; }
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public int? Id { get; set; }
        /// <summary>
        /// Gets or Sets StartTimeOffset
        /// </summary>
        [DataMember(Name="startTimeOffset", EmitDefaultValue=false)]
        public int? StartTimeOffset { get; set; }
        /// <summary>
        /// Gets or Sets EndTimeOffset
        /// </summary>
        [DataMember(Name="endTimeOffset", EmitDefaultValue=false)]
        public int? EndTimeOffset { get; set; }
        /// <summary>
        /// Gets or Sets ChapterName
        /// </summary>
        [DataMember(Name="chapterName", EmitDefaultValue=false)]
        public string ChapterName { get; set; }
        /// <summary>
        /// Gets or Sets TotalSize
        /// </summary>
        [DataMember(Name="totalSize", EmitDefaultValue=false)]
        public int? TotalSize { get; set; }
        /// <summary>
        /// Gets or Sets CompositeContentId
        /// </summary>
        [DataMember(Name="compositeContentId", EmitDefaultValue=false)]
        public int? CompositeContentId { get; set; }
        /// <summary>
        /// Gets or Sets CompositeContentStatus
        /// </summary>
        [DataMember(Name="compositeContentStatus", EmitDefaultValue=false)]
        public string CompositeContentStatus { get; set; }
        /// <summary>
        /// Gets or Sets ParentRecordingId
        /// </summary>
        [DataMember(Name="parentRecordingId", EmitDefaultValue=false)]
        public int? ParentRecordingId { get; set; }
        /// <summary>
        /// Gets or Sets ViewCount
        /// </summary>
        [DataMember(Name="viewCount", EmitDefaultValue=false)]
        public int? ViewCount { get; set; }
        /// <summary>
        /// Gets or Sets RecordingSessions
        /// </summary>
        [DataMember(Name="recordingSessions", EmitDefaultValue=false)]
        public List<RecordingRecordingSessions> RecordingSessions { get; set; }
        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class RecordingRecordingChapters {\n");
            sb.Append("  ChapterId: ").Append(ChapterId).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  StartTimeOffset: ").Append(StartTimeOffset).Append("\n");
            sb.Append("  EndTimeOffset: ").Append(EndTimeOffset).Append("\n");
            sb.Append("  ChapterName: ").Append(ChapterName).Append("\n");
            sb.Append("  TotalSize: ").Append(TotalSize).Append("\n");
            sb.Append("  CompositeContentId: ").Append(CompositeContentId).Append("\n");
            sb.Append("  CompositeContentStatus: ").Append(CompositeContentStatus).Append("\n");
            sb.Append("  ParentRecordingId: ").Append(ParentRecordingId).Append("\n");
            sb.Append("  ViewCount: ").Append(ViewCount).Append("\n");
            sb.Append("  RecordingSessions: ").Append(RecordingSessions).Append("\n");
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
            return this.Equals(obj as RecordingRecordingChapters);
        }

        /// <summary>
        /// Returns true if RecordingRecordingChapters instances are equal
        /// </summary>
        /// <param name="other">Instance of RecordingRecordingChapters to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(RecordingRecordingChapters other)
        {
            // credit: http://stackoverflow.com/a/10454552/677735
            if (other == null)
                return false;

            return 
                (
                    this.ChapterId == other.ChapterId ||
                    this.ChapterId != null &&
                    this.ChapterId.Equals(other.ChapterId)
                ) && 
                (
                    this.Id == other.Id ||
                    this.Id != null &&
                    this.Id.Equals(other.Id)
                ) && 
                (
                    this.StartTimeOffset == other.StartTimeOffset ||
                    this.StartTimeOffset != null &&
                    this.StartTimeOffset.Equals(other.StartTimeOffset)
                ) && 
                (
                    this.EndTimeOffset == other.EndTimeOffset ||
                    this.EndTimeOffset != null &&
                    this.EndTimeOffset.Equals(other.EndTimeOffset)
                ) && 
                (
                    this.ChapterName == other.ChapterName ||
                    this.ChapterName != null &&
                    this.ChapterName.Equals(other.ChapterName)
                ) && 
                (
                    this.TotalSize == other.TotalSize ||
                    this.TotalSize != null &&
                    this.TotalSize.Equals(other.TotalSize)
                ) && 
                (
                    this.CompositeContentId == other.CompositeContentId ||
                    this.CompositeContentId != null &&
                    this.CompositeContentId.Equals(other.CompositeContentId)
                ) && 
                (
                    this.CompositeContentStatus == other.CompositeContentStatus ||
                    this.CompositeContentStatus != null &&
                    this.CompositeContentStatus.Equals(other.CompositeContentStatus)
                ) && 
                (
                    this.ParentRecordingId == other.ParentRecordingId ||
                    this.ParentRecordingId != null &&
                    this.ParentRecordingId.Equals(other.ParentRecordingId)
                ) && 
                (
                    this.ViewCount == other.ViewCount ||
                    this.ViewCount != null &&
                    this.ViewCount.Equals(other.ViewCount)
                ) && 
                (
                    this.RecordingSessions == other.RecordingSessions ||
                    this.RecordingSessions != null &&
                    this.RecordingSessions.SequenceEqual(other.RecordingSessions)
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
                if (this.ChapterId != null)
                    hash = hash * 59 + this.ChapterId.GetHashCode();
                if (this.Id != null)
                    hash = hash * 59 + this.Id.GetHashCode();
                if (this.StartTimeOffset != null)
                    hash = hash * 59 + this.StartTimeOffset.GetHashCode();
                if (this.EndTimeOffset != null)
                    hash = hash * 59 + this.EndTimeOffset.GetHashCode();
                if (this.ChapterName != null)
                    hash = hash * 59 + this.ChapterName.GetHashCode();
                if (this.TotalSize != null)
                    hash = hash * 59 + this.TotalSize.GetHashCode();
                if (this.CompositeContentId != null)
                    hash = hash * 59 + this.CompositeContentId.GetHashCode();
                if (this.CompositeContentStatus != null)
                    hash = hash * 59 + this.CompositeContentStatus.GetHashCode();
                if (this.ParentRecordingId != null)
                    hash = hash * 59 + this.ParentRecordingId.GetHashCode();
                if (this.ViewCount != null)
                    hash = hash * 59 + this.ViewCount.GetHashCode();
                if (this.RecordingSessions != null)
                    hash = hash * 59 + this.RecordingSessions.GetHashCode();
                return hash;
            }
        }
    }

}
