<?php
/**
 * MeetingHistorySharing
 *
 * PHP version 5
 *
 * @category Class
 * @package  BlueJeansOnVideoRestApi
 * @author   Swaagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * BlueJeans onVideo REST API
 *
 * _Video That Works Where You Do._  This site provides developers access to API's from BlueJean's onVideo meeting service.  From here you will be able to make actual API calls to manage User Accounts, Meetings, and Recordings.  Also, you can pull analytical data as well retrieve current state information.  With these API's  you should be able to quickly integrate **BlueJeans** video into your applications.     # Authentication All API transactions (excluding Authentication) require an access token per **OAuth standards**.  BlueJeans provides multiple methods for obtaining an access token.  Additionally there are diffferent scopes of token access. ## Grant Types Bluejeans provides 4 different methods for users to Authenticate.  Successful authentication allows BlueJeans to grant an access token to perform operations. * Password Credentials Grant – Authenticate with a username and password and receive an access token with user level permission. Known as two-legged OAuth. * Meeting Credentials Grant – Authenticate with a meeting ID and meeting passcode and receive an access token with meeting level permission. Known as two-legged OAuth. * Client Credentials Grant –  Authenticate with a client ID and client secret and receive an access token with enterprise level permission. Known as two-legged OAuth. * Authorization Code Grant – After creating a developer application, users witll authenticate via a BlueJeans page, and receive an authorization code. Submit authorization with other tokens and receive an access token. Known as three-legged OAuth. ## Access & Permissions BlueJeans defines 3 levels of API access into the system.  When an access token is granted, it carries one of these 3 levels.  The scope of system functionality depends upon the token's access level. * Meeting-level – Scope of APIs is limited to individual meetings. * User-level – Scope depends on the requested permissions. * App-level – provisioned either by BlueJeans personnel, or the BlueJeans Enterprise Admin, an app, is issued a client key and secret key. These tokens then are used by the BlueJeans Authentication API to receive the token. The token's scope provides access to the entire enterprise and all of its users. All endpoints in this document that require **Enterprise Admin** access will be marked as such. # Getting Started Before you start using the API's on this site, you must first have a BlueJeans account.  With your BlueJean credentials, use one of the Authentication methods to obtain an access token. - Click on the Authorize button at the top of page - Enter your access token in the field marked \"api_key\" Now the web site will automatically include your access token on all API calls you make.
 *
 * OpenAPI spec version: 1.0.0
 * Contact: brandon@bluejeans.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 *
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace BlueJeansOnVideoRestApi\Model;

use \ArrayAccess;

/**
 * MeetingHistorySharing Class Doc Comment
 *
 * @category    Class
 * @package     BlueJeansOnVideoRestApi
 * @author      Swagger Codegen team
 * @link        https://github.com/swagger-api/swagger-codegen
 */
class MeetingHistorySharing implements ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      * @var string
      */
    protected static $swaggerModelName = 'MeetingHistorySharing';

    /**
      * Array of property to type mappings. Used for (de)serialization
      * @var string[]
      */
    protected static $swaggerTypes = [
        'id' => 'int',
        'meeting_guid' => 'string',
        'owner_id' => 'int',
        'sharing_url' => 'string',
        'recepient_type' => 'string',
        'properties' => 'string',
        'status' => 'string',
        'downloadable' => 'bool',
        'passcode' => 'string',
        'validity' => 'string',
        'created' => 'int',
        'lastmodified' => 'int'
    ];

    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of attributes where the key is the local name, and the value is the original name
     * @var string[]
     */
    protected static $attributeMap = [
        'id' => 'id',
        'meeting_guid' => 'meetingGuid',
        'owner_id' => 'ownerId',
        'sharing_url' => 'sharingUrl',
        'recepient_type' => 'recepientType',
        'properties' => 'properties',
        'status' => 'status',
        'downloadable' => 'downloadable',
        'passcode' => 'passcode',
        'validity' => 'validity',
        'created' => 'created',
        'lastmodified' => 'lastmodified'
    ];


    /**
     * Array of attributes to setter functions (for deserialization of responses)
     * @var string[]
     */
    protected static $setters = [
        'id' => 'setId',
        'meeting_guid' => 'setMeetingGuid',
        'owner_id' => 'setOwnerId',
        'sharing_url' => 'setSharingUrl',
        'recepient_type' => 'setRecepientType',
        'properties' => 'setProperties',
        'status' => 'setStatus',
        'downloadable' => 'setDownloadable',
        'passcode' => 'setPasscode',
        'validity' => 'setValidity',
        'created' => 'setCreated',
        'lastmodified' => 'setLastmodified'
    ];


    /**
     * Array of attributes to getter functions (for serialization of requests)
     * @var string[]
     */
    protected static $getters = [
        'id' => 'getId',
        'meeting_guid' => 'getMeetingGuid',
        'owner_id' => 'getOwnerId',
        'sharing_url' => 'getSharingUrl',
        'recepient_type' => 'getRecepientType',
        'properties' => 'getProperties',
        'status' => 'getStatus',
        'downloadable' => 'getDownloadable',
        'passcode' => 'getPasscode',
        'validity' => 'getValidity',
        'created' => 'getCreated',
        'lastmodified' => 'getLastmodified'
    ];

    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    public static function setters()
    {
        return self::$setters;
    }

    public static function getters()
    {
        return self::$getters;
    }

    const RECEPIENT_TYPE_ENTERPRISE = 'ENTERPRISE';
    const RECEPIENT_TYPE_PUBLIC = 'PUBLIC';
    const STATUS_ACTIVE = 'ACTIVE';
    

    
    /**
     * Gets allowable values of the enum
     * @return string[]
     */
    public function getRecepientTypeAllowableValues()
    {
        return [
            self::RECEPIENT_TYPE_ENTERPRISE,
            self::RECEPIENT_TYPE_PUBLIC,
        ];
    }
    
    /**
     * Gets allowable values of the enum
     * @return string[]
     */
    public function getStatusAllowableValues()
    {
        return [
            self::STATUS_ACTIVE,
        ];
    }
    

    /**
     * Associative array for storing property values
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     * @param mixed[] $data Associated array of property values initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['id'] = isset($data['id']) ? $data['id'] : null;
        $this->container['meeting_guid'] = isset($data['meeting_guid']) ? $data['meeting_guid'] : null;
        $this->container['owner_id'] = isset($data['owner_id']) ? $data['owner_id'] : null;
        $this->container['sharing_url'] = isset($data['sharing_url']) ? $data['sharing_url'] : null;
        $this->container['recepient_type'] = isset($data['recepient_type']) ? $data['recepient_type'] : null;
        $this->container['properties'] = isset($data['properties']) ? $data['properties'] : null;
        $this->container['status'] = isset($data['status']) ? $data['status'] : null;
        $this->container['downloadable'] = isset($data['downloadable']) ? $data['downloadable'] : null;
        $this->container['passcode'] = isset($data['passcode']) ? $data['passcode'] : null;
        $this->container['validity'] = isset($data['validity']) ? $data['validity'] : null;
        $this->container['created'] = isset($data['created']) ? $data['created'] : null;
        $this->container['lastmodified'] = isset($data['lastmodified']) ? $data['lastmodified'] : null;
    }

    /**
     * show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalid_properties = [];

        $allowed_values = ["ENTERPRISE", "PUBLIC"];
        if (!in_array($this->container['recepient_type'], $allowed_values)) {
            $invalid_properties[] = "invalid value for 'recepient_type', must be one of 'ENTERPRISE', 'PUBLIC'.";
        }

        $allowed_values = ["ACTIVE"];
        if (!in_array($this->container['status'], $allowed_values)) {
            $invalid_properties[] = "invalid value for 'status', must be one of 'ACTIVE'.";
        }

        return $invalid_properties;
    }

    /**
     * validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {

        $allowed_values = ["ENTERPRISE", "PUBLIC"];
        if (!in_array($this->container['recepient_type'], $allowed_values)) {
            return false;
        }
        $allowed_values = ["ACTIVE"];
        if (!in_array($this->container['status'], $allowed_values)) {
            return false;
        }
        return true;
    }


    /**
     * Gets id
     * @return int
     */
    public function getId()
    {
        return $this->container['id'];
    }

    /**
     * Sets id
     * @param int $id
     * @return $this
     */
    public function setId($id)
    {
        $this->container['id'] = $id;

        return $this;
    }

    /**
     * Gets meeting_guid
     * @return string
     */
    public function getMeetingGuid()
    {
        return $this->container['meeting_guid'];
    }

    /**
     * Sets meeting_guid
     * @param string $meeting_guid
     * @return $this
     */
    public function setMeetingGuid($meeting_guid)
    {
        $this->container['meeting_guid'] = $meeting_guid;

        return $this;
    }

    /**
     * Gets owner_id
     * @return int
     */
    public function getOwnerId()
    {
        return $this->container['owner_id'];
    }

    /**
     * Sets owner_id
     * @param int $owner_id Numeric user ID for the meeting owner.
     * @return $this
     */
    public function setOwnerId($owner_id)
    {
        $this->container['owner_id'] = $owner_id;

        return $this;
    }

    /**
     * Gets sharing_url
     * @return string
     */
    public function getSharingUrl()
    {
        return $this->container['sharing_url'];
    }

    /**
     * Sets sharing_url
     * @param string $sharing_url
     * @return $this
     */
    public function setSharingUrl($sharing_url)
    {
        $this->container['sharing_url'] = $sharing_url;

        return $this;
    }

    /**
     * Gets recepient_type
     * @return string
     */
    public function getRecepientType()
    {
        return $this->container['recepient_type'];
    }

    /**
     * Sets recepient_type
     * @param string $recepient_type
     * @return $this
     */
    public function setRecepientType($recepient_type)
    {
        $allowed_values = array('ENTERPRISE', 'PUBLIC');
        if (!is_null($recepient_type) && (!in_array($recepient_type, $allowed_values))) {
            throw new \InvalidArgumentException("Invalid value for 'recepient_type', must be one of 'ENTERPRISE', 'PUBLIC'");
        }
        $this->container['recepient_type'] = $recepient_type;

        return $this;
    }

    /**
     * Gets properties
     * @return string
     */
    public function getProperties()
    {
        return $this->container['properties'];
    }

    /**
     * Sets properties
     * @param string $properties
     * @return $this
     */
    public function setProperties($properties)
    {
        $this->container['properties'] = $properties;

        return $this;
    }

    /**
     * Gets status
     * @return string
     */
    public function getStatus()
    {
        return $this->container['status'];
    }

    /**
     * Sets status
     * @param string $status
     * @return $this
     */
    public function setStatus($status)
    {
        $allowed_values = array('ACTIVE');
        if (!is_null($status) && (!in_array($status, $allowed_values))) {
            throw new \InvalidArgumentException("Invalid value for 'status', must be one of 'ACTIVE'");
        }
        $this->container['status'] = $status;

        return $this;
    }

    /**
     * Gets downloadable
     * @return bool
     */
    public function getDownloadable()
    {
        return $this->container['downloadable'];
    }

    /**
     * Sets downloadable
     * @param bool $downloadable
     * @return $this
     */
    public function setDownloadable($downloadable)
    {
        $this->container['downloadable'] = $downloadable;

        return $this;
    }

    /**
     * Gets passcode
     * @return string
     */
    public function getPasscode()
    {
        return $this->container['passcode'];
    }

    /**
     * Sets passcode
     * @param string $passcode
     * @return $this
     */
    public function setPasscode($passcode)
    {
        $this->container['passcode'] = $passcode;

        return $this;
    }

    /**
     * Gets validity
     * @return string
     */
    public function getValidity()
    {
        return $this->container['validity'];
    }

    /**
     * Sets validity
     * @param string $validity
     * @return $this
     */
    public function setValidity($validity)
    {
        $this->container['validity'] = $validity;

        return $this;
    }

    /**
     * Gets created
     * @return int
     */
    public function getCreated()
    {
        return $this->container['created'];
    }

    /**
     * Sets created
     * @param int $created A [UNIX Timestamp](https://currentmillis.com/) in milliseconds
     * @return $this
     */
    public function setCreated($created)
    {
        $this->container['created'] = $created;

        return $this;
    }

    /**
     * Gets lastmodified
     * @return int
     */
    public function getLastmodified()
    {
        return $this->container['lastmodified'];
    }

    /**
     * Sets lastmodified
     * @param int $lastmodified A [UNIX Timestamp](https://currentmillis.com/) in milliseconds
     * @return $this
     */
    public function setLastmodified($lastmodified)
    {
        $this->container['lastmodified'] = $lastmodified;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     * @param  integer $offset Offset
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     * @param  integer $offset Offset
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     * @param  integer $offset Offset
     * @param  mixed   $value  Value to be set
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     * @param  integer $offset Offset
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(\BlueJeansOnVideoRestApi\ObjectSerializer::sanitizeForSerialization($this), JSON_PRETTY_PRINT);
        }

        return json_encode(\BlueJeansOnVideoRestApi\ObjectSerializer::sanitizeForSerialization($this));
    }
}


